"""Refresh the public tool snapshot from a clean monorepo actions catalog."""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def render_tools(catalog):
    tools = catalog['tools']
    toolsets = ', '.join(sorted({tool['toolset'] for tool in tools}))
    lines = [
        '# Genfeed MCP tools', '',
        'Generated from the assembled curated MCP catalog in `genfeedai/genfeed.ai`.',
        f"Source actions revision: `{catalog['sourceRevision']}`.", '',
        f'Count: {len(tools)}. Toolsets: {toolsets}.', '',
        'Live schemas and caller permissions take precedence. Use `find_tools` with `name` for a full input schema, role and mutation policy.', '',
        "Approval means `mutationPolicy: 'approval-required'`. A pending approval is not a completed action. `resolve_approval` requires an authorized reviewer and the user's decision.", '',
        '| Tool | Toolset | Role | Required | Approval | Description |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    for tool in tools:
        required = ', '.join(f'`{name}`' for name in tool['required']) or '—'
        approval = 'yes' if tool['mutationPolicy'] == 'approval-required' else 'no'
        description = tool['description'].replace('|', '\\|').replace('\n', ' ')
        lines.append(f"| `{tool['name']}` | {tool['toolset']} | {tool['requiredRole']} | {required} | {approval} | {description} |")
    return '\n'.join(lines) + '\n'


def refresh(monorepo):
    monorepo = monorepo.resolve()
    dirty = subprocess.check_output(
        ['git', '-C', str(monorepo), 'status', '--porcelain', '--', 'packages/actions/src'],
        text=True,
    )
    if dirty.strip():
        raise ValueError('Commit actions catalog changes before recording its source revision.')
    revision = subprocess.check_output(
        ['git', '-C', str(monorepo), 'log', '-1', '--format=%H', '--', 'packages/actions/src'],
        text=True,
    ).strip()
    module = monorepo / 'packages/actions/src/registry/tool-registry.ts'
    source = f'const {{getToolsForSurface}} = await import({json.dumps(str(module))}); console.log(JSON.stringify(getToolsForSurface("mcp")));'
    definitions = json.loads(subprocess.check_output(['bun', '-e', source], cwd=monorepo, text=True))
    tools = [{
        'name': tool['name'],
        'toolset': tool['toolset'],
        'requiredRole': tool['requiredRole'],
        'required': tool['parameters'].get('required', []),
        'mutationPolicy': tool.get('mutationPolicy'),
        'description': tool['description'],
    } for tool in definitions]
    tools.sort(key=lambda tool: (tool['toolset'], tool['name']))
    catalog = {'sourceRepository': 'genfeedai/genfeed.ai', 'sourceRevision': revision, 'tools': tools}
    reference = ROOT / 'skills/genfeed/references'
    (reference / 'tool-catalog.json').write_text(json.dumps(catalog, indent=2) + '\n')
    (reference / 'tools.md').write_text(render_tools(catalog))
    print(f'Refreshed {len(tools)} MCP tools from actions revision {revision}.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('monorepo', type=Path)
    refresh(parser.parse_args().monorepo)
