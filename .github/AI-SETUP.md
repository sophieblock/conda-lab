# AI setup for conda-lab

This repository includes VS Code/Copilot configuration tuned for conda packaging, plugins, and documentation work.

## What’s configured

- `.vscode/settings.json`: editor + Copilot defaults
- `.vscode/mcp.json`: MCP server definitions
- `prompts/Plan.agent.md`: planning agent for conda tasks
- `prompts/*.instructions.md`: auto-applied guidance for recipes, plugins, and workflows
- `.github/workflows/build-recipes.yml`: CI for recipe builds on macOS arm64

## Quick start (Copilot Chat)

- Plan work: `@Plan Create a conda recipe for numpy 2.0 (macOS arm64)`
- Implement: `@workspace Implement the approved plan`
- Review: select files → `@workspace /reviewSelection`

## Automatic instructions

| Files edited | Instructions applied |
| --- | --- |
| `recipes/**/meta.yaml`, `recipes/**/build.sh`, `recipes/**/conda_build_config.yaml` | `prompts/conda-build.instructions.md` |
| `plugins/**/pyproject.toml`, `plugins/**/*.py` | `prompts/conda-plugin.instructions.md` |
| `.github/**/*.yml`, `.github/**/*.yaml` | `prompts/github-actions.instructions.md` |

## MCP servers

MCP servers are defined in `.vscode/mcp.json`. Prefer tools that are already installed in your environment (e.g., a Python module or a standalone executable).

Example (Python-based server):

```json
{
  "servers": {
    "your-server": {
      "command": "python",
      "args": ["-m", "your_mcp_package"],
      "type": "stdio"
    }
  }
}
```

Optional: if you use a Node-based MCP server, you can run it with `npx`, but Node is **not** required for this repo’s default setup.

## Plan agent

Use `@Plan` to get a conda-focused plan (variants, macOS arm64, recipe conventions). Review the plan before handing off to implementation.

## CI workflow

The workflow at `.github/workflows/build-recipes.yml` builds recipes on PRs and pushes to `main` for macOS 14 (arm64). Keep references to this path accurate in new docs.

## Safety

- Do **not** commit secrets or API keys.
- Use local environment variables or GitHub Actions secrets for credentials.

## Related

- [Workspace settings](WORKSPACE-SETTINGS.md)
