# Using conda-lab

This repository is a **conda experimentation sandbox** for learning about conda-build recipes, plugins, and reproducibility on macOS arm64.

## What this repo is

- **Conda recipes** that demonstrate packaging patterns (C, Python, variants)
- **Conda plugins** rebuilt using entry points to study the plugin boundary
- **Documentation** explaining conda-build phases, variants, and reproducibility
- **Lightweight sandbox** — not a framework, SDK, or upstream fork

## What this repo is NOT

- Not a CI/CD pipeline for publishing packages
- Not a conda or conda-build fork
- Not a general-purpose build system

## Core principle

Treat **conda/conda-build as black boxes** (executables we call).  
Study **recipes, plugins, and docs as white boxes** (code we experiment with).

## Quick start

1. Create the environment:
   ```bash
   conda env create -f envs/dev.yml
   conda activate conda-lab-dev
   ```

2. Build a recipe:
   ```bash
   conda build recipes/hello-python/
   ```

3. Experiment with variants:
   ```bash
   conda render recipes/variants-demo/
   ```

4. Install a plugin:
   ```bash
   cd plugins/rebuilt-conda-graph/
   pip install -e .
   conda info --plugins
   ```

## VS Code tasks

Optional: Use VS Code tasks (`.vscode/tasks.json`) for quick builds:
- "conda: build hello-python"
- "conda: build hello-c"  
- "conda: render variants-demo"

Tasks assume you have activated `conda-lab-build` environment.

## MCP configuration (optional)

If you use Model Context Protocol tools, you can add local `.vscode/mcp.json` configuration. This is **optional** and **language-agnostic**. Example:

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

Do **not** commit secrets or tokens to the repository.
