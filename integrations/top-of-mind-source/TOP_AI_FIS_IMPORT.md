# TOP AI FIS Import Note

This folder is a preserved source import from:

`D:\GitHub\Top-of-Mind`

It contains the React cockpit for the future TOP AI FIS web app.

## Useful Parts

| Source Area | TOP AI FIS Role |
| --- | --- |
| `apps/desk` | Primary React cockpit candidate |
| `frontend/top-of-mind` | Earlier/smaller React frontend candidate |
| `src/lib/api/topOfMindApi.js` | Current frontend API contract |
| `docs/ahk-react-api-contract.md` | AHK/React/API bridge contract |
| `wrangler.toml` | Cloudflare Pages/Workers deployment clue |

## Merge Direction

Recommended extraction path:

1. Keep this folder as the source import.
2. Promote `apps/desk` into `apps/web` when ready.
3. Align `apps/api` endpoints with `topOfMindApi.js`.
4. Serve React at `/`.
5. Serve the hub API at `/api` on the Synology/domain deployment.

## Important

React is the cockpit. It should not call provider APIs directly. The hub API owns
provider keys, permissions, memory access, command approval, dispatch, and AHK
bridge jobs.

