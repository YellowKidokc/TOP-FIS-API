# TOP AI FIS Import Note

This folder is a preserved source import from:

`D:\CHI PARTS\FIS\organize`

This is the clean GitHub-ready file organization engine candidate. It is based
on the open-source `organize` style project and has a real package layout,
docs, tests, actions, filters, Dockerfile, and CI config.

## Why Keep This One

This source is useful because it already has:

- safe simulation-before-action workflows
- move/copy/rename/delete/trash/write/shell actions
- extension/name/regex/hash/duplicate/content/EXIF filters
- conflict handling
- tests
- documentation
- Docker/GitHub project structure

## TOP AI FIS Role

Use this as the action/organization engine reference.

The hub should still own:

- permissions
- approval gates
- action proposals
- audit history
- API routing
- memory and file indexing

This engine can later become a worker behind the hub after we wrap it with our
approval and dry-run rules.

## Safety Rule

Do not let this engine run destructive actions directly from a watcher. Watchers
report events. The hub proposes actions. Organization actions execute only after
approval or a clearly safe rule.

