"""Report whether the tool snapshot is behind the latest genfeedai/genfeed.ai release."""
import json
import os
from pathlib import Path
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'genfeedai/genfeed.ai'
CATALOG_PATH = 'packages/actions/src'


def fetch_json(url):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'genfeed-agent-tool-snapshot'}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
        return json.load(response)


def release_catalog_revision(fetch=fetch_json):
    """Return the release tag and the last commit that changed the catalog at that tag."""
    api = f'https://api.github.com/repos/{SOURCE}'
    tag = fetch(f'{api}/releases/latest')['tag_name']
    commits = fetch(f'{api}/commits?sha={tag}&path={CATALOG_PATH}&per_page=1')
    if not commits:
        raise ValueError(f'No commit touching {CATALOG_PATH} found at {tag}.')
    return tag, commits[0]['sha']


def snapshot_revision(root=ROOT):
    catalog = json.loads((root / 'skills/genfeed/references/tool-catalog.json').read_text())
    return catalog['sourceRevision']


def check(fetch=fetch_json, root=ROOT):
    tag, expected = release_catalog_revision(fetch)
    recorded = snapshot_revision(root)
    if recorded == expected:
        return True, f'Tool snapshot matches {SOURCE} {tag} (catalog revision {expected}).'
    return False, (
        f'Tool snapshot is behind {SOURCE} {tag}: recorded catalog revision {recorded}, '
        f'release catalog revision {expected}. Check out {tag} in the main repo and run '
        '`python3 scripts/refresh_tools.py <main repo checkout>`.'
    )


if __name__ == '__main__':
    is_current, message = check()
    print(message)
    sys.exit(0 if is_current else 1)
