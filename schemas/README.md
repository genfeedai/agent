# Upstream validation schemas

Unmodified snapshots of official Agent Plugins, Cursor, and MCP Registry schemas.
`sources.json` records origin, retrieval date and SHA-256. CI uses these local copies,
so validation never fetches or executes remote schema content. To refresh, download
from the official source, inspect the diff, update the digest, and rerun validation.
Upstream licensing applies to these schema documents. These snapshots are validation
inputs and are not shipped in the plugin archive.
