# TOP AI FIS Import Note

This folder is a preserved source import from:

`D:\GitHub\File-intelligent-hub\file-intelligence-hub`

It appears to be an earlier File Intelligence Hub implementation that later fed
into `Top-of-Mind-API`.

## Status

Do not promote this over `D:\GitHub\TOP AI FIS\apps\api`.

The active API copy from `Top-of-Mind-API` has newer pieces that this source does
not include:

- `routes_file_cache.py`
- `routes_folders.py`
- `security.py`

## Useful Parts

| Source Area | TOP AI FIS Role |
| --- | --- |
| `file_intelligence_hub/workers` | Worker lineage and deterministic job logic |
| `file_intelligence_hub/watchers` | Watcher lineage |
| `file_intelligence_hub/intelligence` | File/folder feature builders |
| `docs` | Older API, memory, folder-agent, and security notes |
| `seed_and_run.py` | Local seed/demo runner reference |
| `scripts/autohotkey/top_of_mind_bridge.ahk` | Older bridge reference |

## Merge Direction

Use this as a comparison source when improving the tagger, watcher, scanner, or
worker behavior. Prefer the active implementation under `apps/api` for routes and
storage unless this source has a specific missing behavior we want to recover.

