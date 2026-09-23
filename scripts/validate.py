"""Offline package checks. Live client acceptance is a separate manual gate."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

from jsonschema import FormatChecker, validators
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = (
    'plugin.json', 'mcp.json', '.mcp.json', 'server.json', 'gemini-extension.json',
    '.claude-plugin/plugin.json', '.claude-plugin/marketplace.json',
    '.cursor-plugin/plugin.json', '.cursor-plugin/mcp.json',
    '.grok-plugin/plugin.json', '.grok-plugin/marketplace.json',
    '.agents/plugins/marketplace.json',
)
URL_PATTERN = re.compile(r'https?://[^\s)\]>"\x27`]+')
CREDENTIAL_PATTERN = re.compile(
    r'gf_(?:live|test)_|(?:[?&#])(?:api[_-]?key|access[_-]?token|refresh[_-]?token|token|key|secret|password)=|://[^/\s:]+:[^/\s@]+@', re.I
)
SKIP = {'.git', '.venv', '__pycache__', '.worktrees', 'build'}


def read_json(root, name):
    return json.loads((root / name).read_text())


def walk_values(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key, child
            yield from walk_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_values(child)


def validate(root=ROOT):
    errors = []
    docs = {}
    for name in MANIFESTS:
        try:
            docs[name] = read_json(root, name)
            if not isinstance(docs[name], dict):
                raise ValueError('must be an object')
        except (OSError, ValueError) as exc:
            errors.append(f'{name}: {exc}')
    if errors:
        return errors
    for source in read_json(root, 'schemas/sources.json'):
        path = root / 'schemas' / source['file']
        if hashlib.sha256(path.read_bytes()).hexdigest() != source['sha256']:
            errors.append(f'{path.name}: upstream schema digest changed')
    for filename, schema_file in (
        ('plugin.json', 'agent-plugin.schema.json'),
        ('mcp.json', 'agent-mcp.schema.json'),
        ('.cursor-plugin/plugin.json', 'cursor-plugin.schema.json'),
        ('server.json', 'mcp-server.schema.json'),
    ):
        schema = read_json(root, f'schemas/{schema_file}')
        cls = validators.validator_for(schema)
        cls.check_schema(schema)
        for error in cls(schema, format_checker=FormatChecker()).iter_errors(docs[filename]):
            errors.append(f'{filename}: {error.json_path}: {error.message}')
    version = docs['plugin.json']['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        errors.append('plugin.json: version must be a release semver')
    for filename, data in docs.items():
        for key, value in walk_values(data):
            if key == 'version' and value != version:
                errors.append(f'{filename}: version {value} differs from {version}')
    skill = root / 'skills/genfeed/SKILL.md'
    parts = skill.read_text().split('---', 2)
    try:
        front = yaml.safe_load(parts[1]) if len(parts) == 3 and not parts[0].strip() else {}
    except yaml.YAMLError:
        errors.append('SKILL.md: invalid YAML frontmatter')
        front = {}
    if not isinstance(front, dict):
        errors.append('SKILL.md: frontmatter must be a mapping')
        front = {}
    allowed_frontmatter = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
    if set(front) - allowed_frontmatter:
        errors.append('SKILL.md: unsupported portable frontmatter field')
    metadata = front.get('metadata', {})
    if not isinstance(metadata, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in metadata.items()):
        errors.append('SKILL.md: metadata must map strings to strings')
    if not isinstance(metadata, dict):
        metadata = {}
    if not isinstance(front.get('description'), str) or not 1 <= len(front['description']) <= 1024:
        errors.append('SKILL.md: description must be 1-1024 characters')
    if front.get('name') != 'genfeed' or not front.get('description'):
        errors.append('SKILL.md: name and description required')
    if str(metadata.get('version')) != version:
        errors.append('SKILL.md: metadata.version differs from release')
    expected_url = docs['mcp.json']['mcpServers']['genfeed']['url']
    parsed = urlsplit(expected_url)
    if parsed.scheme != 'https' or parsed.netloc != 'mcp.genfeed.ai' or parsed.path != '/mcp':
        errors.append('mcp.json: unexpected public MCP endpoint')
    if parsed.query != 'toolsets=core,scheduler,content,generation,analytics,brand,onboarding':
        errors.append('mcp.json: distribution toolset profile changed')
    connectors = [
        docs['.mcp.json']['mcpServers']['genfeed'],
        docs['.cursor-plugin/mcp.json']['mcpServers']['genfeed'],
        docs['gemini-extension.json']['mcpServers']['genfeed'],
        docs['server.json']['remotes'][0],
    ]
    for entry in connectors:
        if entry.get('url', entry.get('httpUrl')) != expected_url:
            errors.append('connector URL drift')
    if docs['.mcp.json']['mcpServers']['genfeed'].get('type') != 'http':
        errors.append('.mcp.json: native remote transport must be http')
    claude = docs['.claude-plugin/plugin.json']
    entry = docs['.claude-plugin/marketplace.json']['plugins'][0]
    components = {'skills', 'commands', 'agents', 'hooks', 'mcpServers'}
    if entry.get('strict') is False and components.intersection(claude):
        errors.append('Claude strict:false conflicts with plugin components')
    if components.intersection(entry):
        errors.append('Claude marketplace must not duplicate plugin components')
    if entry['source'] != './' or entry['name'] != 'genfeed':
        errors.append('Claude marketplace must point at this package')
    codex = docs['.agents/plugins/marketplace.json']['plugins'][0]
    if codex['source'] != {'source': 'local', 'path': './'}:
        errors.append('Codex marketplace source must point at the repository root')
    if codex['policy'] != {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}:
        errors.append('Codex marketplace must require install-time authentication')
    for filename, data in docs.items():
        for key, value in walk_values(data):
            if key in {'skills', 'mcpServers', 'logo', 'composerIcon'}:
                paths = value if isinstance(value, list) else [value]
                for path in paths:
                    if not isinstance(path, str):
                        continue
                    target = (root / path).resolve()
                    if Path(path).is_absolute() or '..' in Path(path).parts or not target.is_relative_to(root.resolve()) or not target.exists():
                        errors.append(f'{filename}: invalid component path {path}')
    for filename in ['README.md', 'llms-install.md', 'skills/genfeed/SKILL.md', 'GEMINI.md', 'submissions/form-copy.md']:
        urls = [u for u in URL_PATTERN.findall((root / filename).read_text()) if u.startswith('https://mcp.genfeed.ai/mcp?')]
        if not urls or any(u != expected_url for u in urls):
            errors.append(f'{filename}: missing or stale install URL')
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if set(relative.parts) & SKIP or not path.is_file():
            continue
        if path.is_symlink():
            errors.append(f'{relative}: symlinks are not packaged')
            continue
        if path.suffix not in {'.json', '.md', '.yml', '.py', '.txt', '.csv'}:
            continue
        text = path.read_text()
        if any(CREDENTIAL_PATTERN.search(u) for u in URL_PATTERN.findall(text)):
            errors.append(f'{relative}: credential-like URL (value redacted)')
        if path.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in link or link.startswith(('mailto:', '#')):
                    continue
                target = (path.parent / link.split('#')[0]).resolve()
                if not target.is_relative_to(root.resolve()) or not target.exists():
                    errors.append(f'{relative}: broken local link {link}')
    listing = read_json(root, 'submissions/listing.json')
    if len(listing['tagline']) > 55 or len(listing['description']) > 2000:
        errors.append('listing copy exceeds Claude limits')
    interface = docs['plugin.json']['extensions']['com.openai']['interface']
    # Final directory limits are stricter than the portable package schema.
    # https://developers.openai.com/plugins/deploy/submission-errors
    for field, limit in (('displayName', 30), ('shortDescription', 30),
                         ('longDescription', 4000), ('developerName', 80)):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            errors.append(f'OpenAI final submission: {field} must be 1-{limit} characters')
        elif field != 'longDescription' and ('\n' in value or '\r' in value):
            errors.append(f'OpenAI final submission: {field} must be one line')
    if f"| Short description | {listing['tagline']} |" not in (root / 'submissions/form-copy.md').read_text():
        errors.append('portal short description differs from listing')
    if listing['tagline'] != interface.get('shortDescription'):
        errors.append('submission tagline differs from OpenAI short description')
    if docs['plugin.json']['author']['name'] != listing['publisherLegalName'] or interface['developerName'] != listing['publisherLegalName']:
        errors.append('publisher identity differs across manifest and listing')
    if listing['mcpUrl'] != expected_url:
        errors.append('submission listing URL drift')
    return errors


if __name__ == '__main__':
    failures = validate()
    for failure in failures:
        print(f'ERROR: {failure}', file=sys.stderr)
    if failures:
        sys.exit(1)
    print('PASS: official schemas, versions, discovery paths, URLs, skills and submission links')
