# Rebuilt Conda Graph Plugin

A demonstration plugin showing how to extend conda using **entry points only** — without forking conda or importing its internals.

## Plugin Boundary Demonstrated

This plugin demonstrates the **public plugin API boundary**:

✅ **Uses:** `from conda import plugins` (public API)  
✅ **Registers via:** Entry points in `pyproject.toml`  
✅ **Extends:** Solver and subcommand hooks

❌ **Does NOT use:** Deep conda internals like `conda.core.*`, `conda.models.*`, etc.  
❌ **Does NOT fork:** conda or conda-build source code

## Why This Matters

The conda plugin system lets you:
- Add custom solvers without modifying conda's source
- Add custom subcommands (`conda graph`, etc.)
- Study how conda's architecture works from the outside

By staying at the plugin boundary, you can experiment with conda's behavior while maintaining compatibility with upstream releases.

## What's Inside

- **Custom Solver**: `rebuilt-graph` solver (placeholder that delegates to default)
- **Custom Subcommand**: `conda graph` for dependency analysis
- **Entry Point Registration**: Proper `[project.entry-points.conda]` setup

## Installation

From this directory:

```bash
pip install -e .
```

Verify it's registered:

```bash
conda info --plugins
```

## Usage

### Custom Solver

```bash
conda install --solver=rebuilt-graph numpy
```

(Currently delegates to default solver — extend with your own logic)

### Graph Subcommand

```bash
conda graph numpy pandas --show-deps
```

## Architecture

### Entry Point (pyproject.toml)

```toml
[project.entry-points.conda]
conda-graph-rebuilt = "conda_graph_rebuilt.plugin"
```

### Hook Implementation (plugin.py)

```python
from conda import plugins

@plugins.hookimpl
def conda_solvers():
    yield plugins.CondaSolver(name="rebuilt-graph", backend=RebuiltGraphSolver)

@plugins.hookimpl
def conda_subcommands():
    yield plugins.CondaSubcommand(name="graph", action=RebuiltGraphSubcommand)
```

## Extending This Plugin

To add real solver logic:

1. Edit `src/conda_graph_rebuilt/plugin.py`
2. Implement graph traversal in `RebuiltGraphSolver.solve()`
3. Reinstall: `pip install -e .`

Keep imports limited to `conda.plugins` to stay at the plugin boundary.

## References

- [Conda Plugin Documentation](https://docs.conda.io/projects/conda/en/latest/dev-guide/plugins/index.html)
- [Plugin API](https://docs.conda.io/projects/conda/en/latest/api/plugins/index.html)
