# TOP AI FIS Import Note

This folder is a preserved source import from:

`D:\GitHub\Top-of-Mind-API`

It contains the current API/control-plane implementation and deployment notes.

## Promotion

The API app has also been promoted into:

`D:\GitHub\TOP AI FIS\apps\api`

That active API copy is the one to evolve for the TOP AI FIS hub.

## Useful Parts

| Source Area | TOP AI FIS Role |
| --- | --- |
| `apps/api/file_intelligence_hub/api` | FastAPI routes |
| `apps/api/file_intelligence_hub/storage` | SQLite repositories |
| `apps/api/file_intelligence_hub/workers` | worker jobs for commands, parsing, classification, embeddings |
| `apps/api/file_intelligence_hub/watchers` | folder watcher prototypes |
| `apps/api/tests` | regression tests |
| `ahk` and `apps/api/scripts/autohotkey` | AHK bridge/controller references |
| `api_calls` | numbering and routing documents |
| `deploy/synology` | NAS deployment/package references |

## Safety

Runtime databases and package-stage artifacts should not become canonical source.
The new TOP AI FIS layout should use `data/sqlite` for hub databases and
`data/memory` for folder-based memory buckets.

