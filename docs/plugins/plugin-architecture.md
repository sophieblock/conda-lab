# Conda Plugin Architecture

Understanding how conda's plugin system works under the hood.

## Overview

Conda uses a **plugin system** based on `pluggy` that allows extending conda without modifying core code.

```
┌─────────────────┐
│  Conda Core     │
│  (orchestrator) │
└────────┬────────┘
         │
         │ discovers plugins via entry points
         │
    ┌────┴────┬────────────┬──────────┐
    │         │            │          │
┌───▼───┐ ┌──▼──┐  ┌──────▼───┐  ┌──▼─────┐
│Solver │ │Auth │  │Subcommand│  │Channel │
│Plugin │ │Plugin│  │Plugin    │  │Plugin  │
└───────┘ └─────┘  └──────────┘  └────────┘
```

## Plugin Types

### 1. Solver Plugins

Custom dependency resolution algorithms.

```python
from conda import plugins

class MySolver(plugins.CondaSolver):
    def solve(self, specs, *args, **kwargs):
        # Your solver logic here
        return solution

@plugins.hookimpl
def conda_solvers():
    yield plugins.CondaSolver(
        name="my-solver",
        backend=MySolver,
    )
```

Usage:
```bash
conda install --solver=my-solver numpy
```

### 2. Subcommand Plugins

Add new conda commands.

```python
@plugins.hookimpl
def conda_subcommands():
    yield plugins.CondaSubcommand(
        name="my-command",
        summary="Does something useful",
        action=MyCommandClass,
    )
```

Usage:
```bash
conda my-command --option value
```

### 3. Virtual Package Plugins

Report system capabilities.

```python
@plugins.hookimpl
def conda_virtual_packages():
    yield plugins.CondaVirtualPackage(
        name="my_hardware",
        version="1.0",
        build="0",
    )
```

### 4. Post-Command Plugins

Run hooks after conda commands.

```python
@plugins.hookimpl
def conda_post_commands():
    yield plugins.CondaPostCommand(
        name="my-post-hook",
        action=my_hook_function,
        run_for={"install", "update"},
    )
```

## Plugin Discovery

### Entry Points

Plugins register via Python entry points in `setup.py` or `pyproject.toml`:

**setup.py**:
```python
setup(
    name="my-conda-plugin",
    entry_points={
        "conda": [
            "my-plugin=my_plugin.module",
        ],
    },
)
```

**pyproject.toml**:
```toml
[project.entry-points.conda]
my-plugin = "my_plugin.module"
```

### Discovery Process

1. Conda scans installed packages for `conda` entry points
2. Loads plugin modules
3. Calls hook implementations via `pluggy`
4. Caches discovered plugins

View discovered plugins:
```bash
conda info --plugins
```

## Hook System

Conda uses `pluggy` for hook management:

```python
from conda import plugins

# Define a hook implementation
@plugins.hookimpl
def conda_solvers():
    """This hook is called when conda discovers solvers."""
    yield plugins.CondaSolver(...)

@plugins.hookimpl
def conda_subcommands():
    """This hook is called when conda builds its CLI."""
    yield plugins.CondaSubcommand(...)
```

### Hook Specification

Hooks are defined in conda's codebase:

```python
# In conda/plugins/hookspec.py
@hookspec
def conda_solvers():
    """Return custom solver implementations."""

@hookspec  
def conda_subcommands():
    """Return custom subcommands."""
```

## Plugin Lifecycle

```
1. Package Installation
   └─> Plugin installed via pip/conda

2. Plugin Discovery
   └─> Conda scans entry points on startup

3. Hook Registration
   └─> pluggy registers all @hookimpl functions

4. Hook Execution
   └─> Conda calls hooks at appropriate times

5. Plugin Execution
   └─> Your plugin code runs
```

## Best Practices

### 1. Namespace Your Plugin

```python
# Good: Scoped name
name="my-org-solver"

# Bad: Generic name
name="solver"
```

### 2. Handle Errors Gracefully

```python
def solve(self, specs, *args, **kwargs):
    try:
        return self._solve_impl(specs)
    except Exception as e:
        # Log error and fall back
        logger.error(f"Solver failed: {e}")
        return super().solve(specs, *args, **kwargs)
```

### 3. Document Plugin Behavior

```python
class MySolver(plugins.CondaSolver):
    """
    Custom solver using algorithm X.
    
    Features:
    - Optimizes for Y
    - Handles Z differently
    
    Usage:
        conda install --solver=my-solver package
    """
```

### 4. Version Your Plugin API

```python
setup(
    name="my-plugin",
    version="1.0.0",
    install_requires=[
        "conda>=23.1.0,<24.0",  # Pin compatible conda versions
    ],
)
```

## Testing Plugins

### Unit Tests

```python
import pytest
from conda import plugins

def test_solver_registration():
    solver = list(conda_solvers())[0]
    assert solver.name == "my-solver"
    
def test_solver_logic():
    solver = MySolver()
    result = solver.solve(["numpy"])
    assert result is not None
```

### Integration Tests

```bash
# Install plugin
pip install -e .

# Verify registration
conda info --plugins | grep my-plugin

# Test functionality
conda install --solver=my-solver numpy
```

## Debugging

### Enable Plugin Debug Logging

```bash
export CONDA_VERBOSITY=3
conda install numpy
```

### List Loaded Plugins

```bash
conda info --plugins
```

### Inspect Plugin Entry Points

```bash
python -c "
from importlib.metadata import entry_points
eps = entry_points()
for ep in eps.get('conda', []):
    print(ep.name, '->', ep.value)
"
```

## Example Plugin Structure

```
my-conda-plugin/
├── pyproject.toml           # Package metadata + entry points
├── src/
│   └── my_conda_plugin/
│       ├── __init__.py
│       └── plugin.py        # Hook implementations
├── tests/
│   └── test_plugin.py
└── README.md
```

## References

- [Conda Plugin Guide](https://docs.conda.io/projects/conda/en/latest/dev-guide/plugins/index.html)
- [Plugin API Reference](https://docs.conda.io/projects/conda/en/latest/api/plugins/index.html)
- [pluggy Documentation](https://pluggy.readthedocs.io/)
- [Python Entry Points](https://packaging.python.org/en/latest/specifications/entry-points/)

## See Also

- `plugins/rebuilt-conda-graph/` - Example plugin implementation
- `docs/plugins/entry-points.md` - Deep dive on entry points
