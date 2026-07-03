# Workers

Workers do the heavier jobs behind the hub API.

| Worker Area | Role |
| --- | --- |
| `chunkers` | Split text, documents, clipboard, and messages into chunks |
| `embeddings` | Create/store/search vector embeddings |
| `dispatch` | Route messages to agents, desktop bridges, and API targets |
| `commands` | Run approved command-line jobs and capture output |
| `mcp` | Register and call approved MCP tools |
| `knowledge` | Index and search memory buckets / knowledge banks |

Workers should be callable from the API. They should not bypass the hub permission layer.

