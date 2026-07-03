# Integrations

Integrations are connector packages for systems outside the hub.

Planned lanes:

- `obs/`: OBS plugin/API connector.
- `nas/`: NAS/shared storage connector.
- `syncthing/`: Syncthing API connector.
- `cloudflare-r2/`: R2 media/object storage connector.
- `webdav/`: WebDAV file API connector.

Each integration should declare:

- API URL or local bridge requirement
- capabilities
- auth method using `secret_ref`
- safe actions
- review-required actions
