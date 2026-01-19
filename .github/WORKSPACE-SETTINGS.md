# VS Code workspace settings

This repo uses folder-level settings in `.vscode/settings.json` plus an optional multi-root workspace file at `workspace/conda-lab.code-workspace`.

## Precedence (highest wins)

1. Folder settings (`.vscode/settings.json`)
2. Workspace settings (`workspace/conda-lab.code-workspace`)
3. User settings
4. Default settings

Folder settings are the most specific and will override workspace-level settings for files in this repo.

## Current layout

- `workspace/conda-lab.code-workspace` includes the repo folder and does not define settings yet.
- `.vscode/settings.json` contains the shared Copilot and editor defaults.

## Where to change things

- **Shared settings for the repo:** edit `.vscode/settings.json`.
- **Personal or multi-root overrides:** edit `workspace/conda-lab.code-workspace` (keep personal changes out of version control if needed).

## Tasks, launch, and MCP

- Tasks and launch configs can live in `.vscode/` or in the workspace file. Folder-level entries apply to this repo when it is part of a multi-root workspace.
- MCP servers are defined in `.vscode/mcp.json` and load whenever this folder is opened (directly or via the workspace file).
