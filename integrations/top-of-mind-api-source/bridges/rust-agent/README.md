# Rust Agent

Future stronger background agent for each Windows machine.

Responsibilities:

- poll the hub API
- manage long-running bridge state
- call AutoHotkey or Windows APIs for local UI control
- manage local logs
- eventually host OCR/window-follow services

AutoHotkey is still the fastest first bridge. Rust comes later when the workflow is proven.
