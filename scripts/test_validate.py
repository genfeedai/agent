"""Regression checks for the manifest defects that prompted this release."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from validate import ROOT, validate


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '.venv', 'build', '__pycache__', '.worktrees'))

    def change(self, name, update):
        path = self.root / name
        data = json.loads(path.read_text())
        update(data)
        path.write_text(json.dumps(data))

    def test_portable_unknown_field_rejected(self):
        self.change('plugin.json', lambda d: d.update(skills='./skills'))
        self.assertTrue(any('Additional properties' in e for e in validate(self.root)))

    def test_claude_component_conflict_rejected(self):
        self.change('.claude-plugin/marketplace.json', lambda d: d['plugins'][0].update(strict=False))
        self.change('.claude-plugin/plugin.json', lambda d: d.update(skills='./skills'))
        self.assertTrue(any('conflicts' in e for e in validate(self.root)))

    def test_nested_version_drift_rejected(self):
        self.change('.grok-plugin/marketplace.json', lambda d: d['plugins'][0].update(version='0.0.0'))
        self.assertTrue(any('version' in e for e in validate(self.root)))

    def test_connector_drift_rejected(self):
        self.change('.mcp.json', lambda d: d['mcpServers']['genfeed'].update(url='https://mcp.genfeed.ai/mcp'))
        self.assertIn('connector URL drift', validate(self.root))

    def test_path_escape_rejected(self):
        self.change('.cursor-plugin/plugin.json', lambda d: d.update(skills='../outside'))
        self.assertTrue(any('invalid component path' in e for e in validate(self.root)))

    def test_credentials_redacted(self):
        secret = 'private-test-value'
        (self.root / 'bad.md').write_text('https://example.com/?' + 'token=' + secret)
        errors = validate(self.root)
        self.assertTrue(any('credential-like' in e for e in errors))
        self.assertNotIn(secret, '\n'.join(errors))

    def test_nonportable_skill_metadata_rejected(self):
        path = self.root / 'skills/genfeed/SKILL.md'
        path.write_text(path.read_text().replace('metadata:\n', 'metadata:\n  nested: {value: bad}\n'))
        self.assertTrue(any('metadata must' in e for e in validate(self.root)))

    def test_empty_skill_frontmatter_rejected(self):
        path = self.root / 'skills/genfeed/SKILL.md'
        body = path.read_text().split('---', 2)[2]
        path.write_text('---\n---' + body)
        self.assertIn('SKILL.md: frontmatter must be a mapping', validate(self.root))

    def test_scalar_skill_metadata_rejected(self):
        path = self.root / 'skills/genfeed/SKILL.md'
        path.write_text(path.read_text().replace('metadata:\n  version: "0.1.2"', 'metadata: invalid'))
        self.assertIn('SKILL.md: metadata must map strings to strings', validate(self.root))

    def test_invalid_yaml_rejected(self):
        path = self.root / 'skills/genfeed/SKILL.md'
        path.write_text(path.read_text().replace('metadata:', 'metadata: [unterminated'))
        self.assertIn('SKILL.md: invalid YAML frontmatter', validate(self.root))

    def test_package_passes(self):
        self.assertEqual([], validate(self.root))
