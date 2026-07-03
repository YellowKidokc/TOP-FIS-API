# Synology Integration

Planned connector for Synology DSM / File Station.

Use cases:

- list NAS folders
- upload/download files
- move/copy/archive files
- create shared links
- store daily SQLite backups
- serve as a long-term media/document target

Security:

- store only `SYNOLOGY_DSM_TOKEN` or another `secret_ref` in config
- keep the actual credential in Windows Credential Manager, environment variables, or a future vault
- route destructive actions through hub review

The hub API should remain the control point. Other computers should call the hub, not each mutate the NAS independently.
