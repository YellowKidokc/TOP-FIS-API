# TOP AI FIS

TOP AI FIS is the central workspace for the File Intelligence System.

The goal is one hub with many small watchers:

- Desktop, laptop, and Synology watchers report file events.
- The hub stores events, API calls, clipboard history, scans, labels, and actions.
- Scanner, labeler, organizer, converter, NLP, and AI tools are separate lanes the hub can call.
- Destructive actions stay proposal-first until a rule explicitly allows automation.

## First Layout

| Path | Purpose |
| --- | --- |
| `apps/api` | Future FastAPI or service API for the hub |
| `apps/web` | Future React/Top-of-Mind style web UI |
| `apps/desktop` | Future desktop tray or packaged UI |
| `agents/watchers` | File/folder event watchers for machines and folders |
| `agents/scanners` | Folder/file symptom scanners and report generators |
| `agents/labelers` | `.chi`, `.fmeta`, `.fisnote`, and metadata label tools |
| `agents/organizers` | Move/copy/archive/rename proposal engines |
| `agents/converters` | PDF/image/audio/video conversion workers |
| `integrations` | AutoHotkey, Top-of-Mind, Syncthing, Synology, R2, MCP |
| `data/sqlite` | SQLite databases for the hub |
| `data/memory/TopOfMind_Memory` | Folder-based memory buckets |
| `data/cache` | Local cache for API calls, clipboard, file events, scans, NLP |
| `config` | Node, folder, and rule configuration |
| `runtime` | Logs, queues, and temporary runtime state |
| `docs` | Architecture, schemas, operations, and handoff notes |

## Operational Rule

Watchers report. The hub decides. Action engines propose. Approval or explicit safe rules execute.

## Memory Rule

Folders store memory. SQLite indexes memory. The Hub API controls who can see memory.

Do not rely on folder names alone for security. Private agent folders are convenience
storage; the API permission layer is the wall.

## Start Here

For the full install-to-daily-use story, read:

- `docs/operations/end-to-end-walkthrough.md`
- `docs/operations/onboarding-and-background-scan.md`
- `docs/architecture/28pof-workbook-integration.md`
- `docs/architecture/pof-hub-integration-plan.md`
- `docs/architecture/scanner-pipeline.md`
- `docs/architecture/label-enforcement.md`
- `docs/architecture/legacy-fis-semantic-addressing.md`
- `docs/schemas/api-contract-v0.md`
- `docs/schemas/folder-label-example.md`
- `docs/handoffs/forgotten-systems-inventory.md`
