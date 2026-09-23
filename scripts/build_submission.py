"""Build allowlisted, reproducible review artifacts from a clean Git revision."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import zipfile

from validate import ROOT, validate


def archive(path, files):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as output:
        for file in sorted(files):
            entry = zipfile.ZipInfo(file.relative_to(ROOT).as_posix(), (2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            output.writestr(entry, file.read_bytes())


def main():
    failures = validate()
    if failures:
        raise SystemExit('\n'.join(failures))
    status = subprocess.check_output(['git', 'status', '--porcelain'], cwd=ROOT, text=True)
    if status.strip():
        raise SystemExit('Commit the package first; submission artifacts must identify an exact clean revision.')
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    version = json.loads((ROOT / 'plugin.json').read_text())['version']
    output = ROOT / 'build'
    output.mkdir(exist_ok=True)
    files = [ROOT / name for name in (
        'plugin.json', 'mcp.json', '.mcp.json', 'server.json', 'gemini-extension.json',
        'GEMINI.md', 'README.md', 'LICENSE', 'CHANGELOG.md', 'llms-install.md',
        '.claude-plugin/plugin.json', '.claude-plugin/marketplace.json',
        '.cursor-plugin/plugin.json', '.cursor-plugin/mcp.json',
        '.grok-plugin/plugin.json', '.grok-plugin/marketplace.json',
        '.agents/plugins/marketplace.json',
    )]
    for folder in ('skills', 'assets', 'submissions'):
        files.extend(p for p in (ROOT / folder).rglob('*') if p.is_file())
    archive(output / f'genfeed-{version}.zip', files)
    archive(output / f'genfeed-skills-{version}.zip', [p for p in files if p.is_relative_to(ROOT / 'skills')])
    shutil.copytree(ROOT / 'submissions', output / 'submissions', dirs_exist_ok=True)
    shutil.copytree(ROOT / 'assets', output / 'assets', dirs_exist_ok=True)
    entry = {
        'name': 'genfeed', 'description': 'Connect Grok Build to your Genfeed workspace for content, scheduling and analytics.',
        'category': 'productivity',
        'source': {'source': 'url', 'url': 'https://github.com/genfeedai/agent.git', 'sha': sha},
        'homepage': 'https://genfeed.ai', 'keywords': ['genfeed', 'genfeed.ai'],
        'domains': ['genfeed.ai', 'mcp.genfeed.ai'], 'version': version,
    }
    (output / 'grok-catalog-entry.json').write_text(json.dumps(entry, indent=2)+'\n')
    record = {'version': version, 'commit': sha, 'authenticatedAcceptance': 'not-attested-by-build', 'archives': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in output.glob(f'*{version}.zip')}}
    (output / 'release.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
