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


def skill_package_files(files):
    required = {'plugin.json', 'LICENSE'}
    return [file for file in files if file.relative_to(ROOT).as_posix() in required
            or file.relative_to(ROOT).parts[0] in {'skills', 'assets'}]


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
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    files = [ROOT / name for name in (
        'plugin.json', 'mcp.json', '.mcp.json', 'server.json', 'gemini-extension.json',
        'GEMINI.md', 'README.md', 'CONTRIBUTING.md', 'LICENSE', 'CHANGELOG.md', 'llms-install.md',
        '.claude-plugin/plugin.json', '.claude-plugin/marketplace.json',
        '.cursor-plugin/plugin.json', '.cursor-plugin/mcp.json',
        '.grok-plugin/plugin.json', '.grok-plugin/marketplace.json',
        '.agents/plugins/marketplace.json',
    )]
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT, text=True).split('\0')
    for name in tracked:
        if name and Path(name).parts[0] in {'skills', 'assets', 'submissions'}:
            files.append(ROOT / name)
    archive(output / f'genfeed-{version}.zip', files)
    archive(output / f'genfeed-skills-{version}.zip', skill_package_files(files))
    for file in files:
        relative = file.relative_to(ROOT)
        if relative.parts[0] in {'submissions', 'assets'}:
            destination = output / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(file, destination)
    entry = json.loads((ROOT / '.grok-plugin/marketplace.json').read_text())['plugins'][0]
    entry['source'] = {'source': 'url', 'url': 'https://github.com/genfeedai/agent.git', 'sha': sha}
    (output / 'grok-catalog-entry.json').write_text(json.dumps(entry, indent=2)+'\n')
    record = {'version': version, 'commit': sha, 'authenticatedAcceptance': 'not-attested-by-build', 'archives': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in output.glob(f'*{version}.zip')}}
    (output / 'release.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
