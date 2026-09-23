# MCP Registry

The root `server.json` describes `io.github.genfeedai/genfeed` as a hosted
`streamable-http` server. The version matches the plugin release. It is not an npm
package and does not require publishing a local server binary.

Follow the official [remote-server publishing guide](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx)
and the [publisher documentation](https://github.com/modelcontextprotocol/registry/tree/main/docs).
Use the official publisher, authenticate with an identity authorized for the
`genfeedai` GitHub namespace, and validate ownership before publishing `server.json`.
Do not invent registry credentials or a verification token. Record the returned
registry entry and published version; a committed descriptor is not publication.

Registry publication does not automatically publish Cursor, Claude, OpenAI or Grok
listings. It can proceed separately once its own ownership and endpoint checks pass.
