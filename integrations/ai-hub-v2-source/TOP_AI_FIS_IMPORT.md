# TOP AI FIS Import Note

This folder is a preserved source import from:

`D:\GitHub\ai-hub-v2`

It was copied into TOP AI FIS as a legacy/reference implementation for the
desktop control layer. It is not merged into the new hub API yet.

## Useful Parts

| Source Area | TOP AI FIS Role |
| --- | --- |
| `hub_core.ahk` | Legacy AHK GUI, clipboard, prompt, and AI-control behavior |
| `AI-HUB.ahk` | Legacy entry point |
| `sync_server.py` | Old local HTTP bridge pattern |
| `modules/clipboard3.html` | Clipboard UI reference |
| `modules/prompt_picker.html` | Prompt picker UI reference |
| `modules/comms-dashboard.html` | Agent/comms dashboard reference |
| `modules/comms_broadcast.ahk` | Broadcast/interruption reference |
| `command_center/` | Command-line launcher and safe command manifest reference |
| `command_center/scripts/py/preference_capture.py` | First preference-capture seed |
| `BetterTTS/` | OCR, TTS, voice, and screen annotation utilities |

## Merge Direction

Do not copy this wholesale into `apps/api`.

Recommended path:

1. Extract the command manifest idea into `workers/commands`.
2. Extract clipboard UI behavior into `apps/web`.
3. Extract AHK bridge behavior into `integrations/autohotkey`.
4. Extract preference capture into the `preferences` SQLite table.
5. Keep BetterTTS/OCR as a separate worker/integration until stable.

## Safety

This source can contain local settings and old hotkey assumptions. Review before
running. The new TOP AI FIS hub should own API auth, permissions, command
approval, and memory access.

