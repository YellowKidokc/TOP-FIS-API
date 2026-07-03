# TOP AI FIS Import Note

This folder is a preserved source import from:

`D:\DONT TOUCH BOOT UP\filetagger`

Large runtime databases and spreadsheet outputs were intentionally excluded from
the import. The source import is for the file labeler/tagger lineage, not for
moving old catalog databases into the new hub.

## Promoted Pieces

These files were promoted into the active agent lanes:

| Source | Active TOP AI FIS Path |
| --- | --- |
| `filetagger.py` | `agents/labelers/filetagger.py` |
| `foldertagger.py` | `agents/labelers/foldertagger.py` |
| `filetagger_daemon.py` | `agents/watchers/filetagger_daemon.py` |
| `salvaged/file_watcher.py` | `agents/watchers/salvaged_file_watcher.py` |

## Role

This is the missing label/tag layer:

- per-file `.fmeta` sidecars
- per-folder `.folder.fmeta` markers
- `.chi` classification lineage
- always-on watcher/catalog daemon lineage
- WordNet/category expansion experiments

## Rule

Do not inject executable scripts into every file. Use portable sidecar files and
SQLite indexing. The hub can read sidecars, index them, and decide whether to
propose actions.

