# Rebuilt Conda Graph Plugin

A demonstration plugin that rebuilds conda's dependency graph solver as a standalone plugin.

## Purpose

This plugin shows how core conda functionality (specifically the dependency resolver) could be structured as a plugin using conda's plugin architecture. It's intended for:

- **Learning**: Understanding conda's plugin system
- **Experimentation**: Testing alternative solver implementations
- **Documentation**: Demonstrating plugin architecture patterns

## Features

- **Custom Solver**: `rebuilt-graph` solver backend
- **Graph Subcommand**: `conda graph` command for dependency analysis
- **Modern Structure**: Uses pyproject.toml and src/ layout
- **Entry Points**: Properly registers via conda's plugin system

## Installation

### Development Install

From this directory:

```bash
pip install -e .
```

### Production Install

```bash
pip install .
```

Or build and install with conda:

```bash
conda build .
conda install conda-graph-rebuilt
```

## Usage

### Using the Custom Solver

```bash
# Use the rebuilt-graph solver
conda install --solver=rebuilt-graph numpy

# Note: The current implementation delegates to the default solver
# but provides a framework for custom implementations
```

### Using the Graph Subcommand

```bash
# Analyze package dependencies
conda graph numpy pandas --show-deps

# Get help
conda graph --help
```

## Architecture

### Plugin Registration

The plugin registers two components via entry points in `pyproject.toml`:

```toml
[project.entry-points.conda]
conda-graph-rebuilt = "conda_graph_rebuilt.plugin"
```

### Hook Implementations

The plugin implements two conda hooks:

1. **`conda_solvers()`**: Registers a custom solver backend
2. **`conda_subcommands()`**: Registers a new conda subcommand

### Solver Design

The `RebuiltGraphSolver` class demonstrates the solver API:

- Inherits from `plugins.CondaSolver`
- Implements `solve()` method
- Could contain custom graph algorithms

## Development

### Project Structure

```
rebuilt-conda-graph/
├── pyproject.toml          # Modern Python packaging config
├── src/
│   └── conda_graph_rebuilt/
│       ├── __init__.py
│       └── plugin.py       # Plugin implementation
└── README.md
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/
ruff check src/
```

## References

- [Conda Plugin Documentation](https://docs.conda.io/projects/conda/en/latest/dev-guide/plugins/index.html)
- [Conda Solver API](https://docs.conda.io/projects/conda/en/latest/api/plugins/index.html#solvers)
- [Python Packaging Guide](https://packaging.python.org/en/latest/)

## Why "Rebuilt"?

This plugin is named "rebuilt" to emphasize that it demonstrates how conda's existing functionality could be restructured as plugins. It's not meant to replace conda's solver but to show how modular and extensible conda can be through its plugin system.
