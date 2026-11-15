"""The drift check passes on a matching revision and fails on an old one."""
import json
from pathlib import Path
import tempfile
import unittest

from check_tool_snapshot import check

RELEASE_SHA = 'a' * 40
OLD_SHA = 'b' * 40


def fake_fetch(url):
    if url.endswith('/releases/latest'):
        return {'tag_name': 'v9.9.9'}
    assert 'sha=v9.9.9' in url and 'path=packages/actions/src' in url
    return [{'sha': RELEASE_SHA}]


class ToolSnapshotDriftTests(unittest.TestCase):
    def root_with_revision(self, revision):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        reference = root / 'skills/genfeed/references'
        reference.mkdir(parents=True)
        (reference / 'tool-catalog.json').write_text(json.dumps({'sourceRevision': revision, 'tools': []}))
        return root

    def test_matching_revision_is_current(self):
        is_current, message = check(fake_fetch, self.root_with_revision(RELEASE_SHA))
        self.assertTrue(is_current)
        self.assertIn('v9.9.9', message)

    def test_old_revision_is_reported_as_behind(self):
        is_current, message = check(fake_fetch, self.root_with_revision(OLD_SHA))
        self.assertFalse(is_current)
        self.assertIn(OLD_SHA, message)
        self.assertIn(RELEASE_SHA, message)


if __name__ == '__main__':
    unittest.main()
