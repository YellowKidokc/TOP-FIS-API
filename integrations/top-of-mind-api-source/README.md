# Top of Mind

Top of Mind is the local/LAN command desk for AI agents, desktop bridges, memory, files, integrations, and reviewable automation.

## Layout

- `apps/api/`: FastAPI hub brain, SQLite storage, workers, tests, docs, configs, and CLI.
- `apps/desk/`: future React/Vite TypingMind-style frontend.
- `api_calls/`: reusable prompt/API call packs, routing manifests, and vectorization plans.
- `ahk/`: current AutoHotkey controllers and operating guides.
- `bridges/autohotkey/`: future Windows hotkey/type/click/OCR bridge.
- `bridges/rust-agent/`: future stronger background agent.
- `integrations/`: future connector packages for OBS, NAS, Syncthing, R2, WebDAV, and other APIs.

## Current API

The tested API lives in `apps/api`.

Useful routes:

- `/top-of-mind/messages`
- `/top-of-mind/sources`
- `/memory/items`
- `/memory/search`
- `/memory/embed-pending`
- `/files/cache`
- `/files/cache/search`
- `/folders`
- `/operator/file-actions`
- `/operator/commands`
- `/jobs`
- `/reviews`
- `/nodes`

## Run API

```powershell
cd apps/api
py -3.12 -m pytest
fihub-api --host 0.0.0.0 --port 10000
```

For LAN clients, use the machine IP instead of `127.0.0.1`, for example:

```text
http://192.168.2.50:10000
```

## SQLite

The hub uses SQLite by default. Keep the database local to the hub machine and let other machines call the API over the LAN. Do not have multiple computers write directly to the same SQLite file on a network share.

Set a custom DB path with:

```powershell
$env:FIHUB_DB_PATH="D:\TopOfMind\data\top-of-mind.sqlite3"
```

Synology/NAS should be used for backups, archives, and shared files, not as the live SQLite writer.

## Command Line

The API package includes `fihub-top` for plugging scripts and agents into the hub:

```powershell
fihub-top memory-add --title "Vector plan" --body "Embeddings connect memory to prompts." --embed
fihub-top memory-search "memory prompts" --mode vector
fihub-top message-post --source-id clipboard --source-label Clipboard --body "Saved clipboard text"
fihub-top command-post py -3.12 -c "print('hello')" --no-review
```

## Security Rule

Do not store raw passwords or tokens in this repo, SQLite, or normal config files. Store `secret_ref` names and keep the actual secrets in Windows Credential Manager, environment variables, ignored `.env` files, or a future vault.

