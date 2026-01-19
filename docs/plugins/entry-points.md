# Python Entry Points

Entry points are Python's standard mechanism for plugin discovery and extensibility.

## What Are Entry Points?

Entry points allow packages to advertise "hooks" that other packages can discover and use at runtime.

```python
# Package A defines an entry point
setup(
    name="my-plugin",
    entry_points={
        "conda": ["my-plugin=my_plugin:main"]
    }
)

# Package B discovers and uses it
from importlib.metadata import entry_points
eps = entry_points(group="conda")
for ep in eps:
    plugin = ep.load()  # Import and get the object
```

## Entry Point Anatomy

```
group:name = module:attribute
  │     │        │        │
  │     │        │        └─ Python attribute to load
  │     │        └─────────── Python module path
  │     └──────────────────── Entry point name (unique within group)
  └────────────────────────── Entry point group (namespace)
```

### Examples

```python
# Simple function
"console_scripts": ["mytool=mypackage.cli:main"]
#                    └─────┘  └──────────────┘
#                    command   function to call

# Class or object
"conda": ["my-plugin=my_plugin.plugin:PluginClass"]
#         └────────┘  └────────────────────────────┘
#         plugin name  module:class

# Module (no attribute)
"pytest11": ["my-pytest-plugin=my_pytest_plugin"]
#            └────────────────┘ └───────────────┘
#            plugin name        module to import
```

## Configuration Formats

### setup.py

```python
from setuptools import setup

setup(
    name="my-package",
    entry_points={
        "console_scripts": [
            "mytool=mypackage.cli:main",
        ],
        "conda": [
            "my-conda-plugin=mypackage.conda_plugin",
        ],
    },
)
```

### pyproject.toml

```toml
[project.scripts]
mytool = "mypackage.cli:main"

[project.entry-points.conda]
my-conda-plugin = "mypackage.conda_plugin"
```

### setup.cfg (legacy)

```ini
[options.entry_points]
console_scripts =
    mytool = mypackage.cli:main
conda =
    my-conda-plugin = mypackage.conda_plugin
```

## Common Entry Point Groups

### `console_scripts`

Create command-line tools:

```python
entry_points={
    "console_scripts": [
        "hello=mypackage:main",  # Creates 'hello' command
    ],
}
```

After installation:
```bash
hello  # Calls mypackage.main()
```

### `gui_scripts`

Like `console_scripts` but for GUI apps (no console window on Windows):

```python
entry_points={
    "gui_scripts": [
        "myapp=mypackage.gui:main",
    ],
}
```

### Framework-Specific Groups

- **`conda`**: Conda plugins
- **`pytest11`**: Pytest plugins
- **`flask.commands`**: Flask CLI extensions
- **`sphinx.builders`**: Sphinx builders

## Discovery and Loading

### List Entry Points

```python
from importlib.metadata import entry_points

# Get all groups
all_eps = entry_points()

# Get specific group
conda_plugins = entry_points(group="conda")

# Iterate
for ep in conda_plugins:
    print(f"Name: {ep.name}")
    print(f"Value: {ep.value}")
    print(f"Group: {ep.group}")
```

### Load Entry Points

```python
from importlib.metadata import entry_points

# Discover and load
for ep in entry_points(group="conda"):
    plugin_module = ep.load()  # Imports module/loads attribute
    print(f"Loaded: {ep.name} -> {plugin_module}")
```

### Command-Line Inspection

```bash
# List all entry points for a package
python -c "
from importlib.metadata import entry_points
eps = entry_points()
for group_name in eps.groups:
    print(f'[{group_name}]')
    for ep in eps.select(group=group_name):
        print(f'  {ep.name} = {ep.value}')
"
```

## Conda Plugin Entry Points

### Registration

```toml
# pyproject.toml
[project.entry-points.conda]
my-plugin = "my_plugin.plugin"
```

This tells conda: "Load `my_plugin.plugin` module to find hooks."

### Module Structure

```python
# my_plugin/plugin.py
from conda import plugins

@plugins.hookimpl
def conda_solvers():
    """Conda discovers this via the entry point."""
    yield plugins.CondaSolver(...)

@plugins.hookimpl
def conda_subcommands():
    """Another hook in the same entry point."""
    yield plugins.CondaSubcommand(...)
```

### Discovery Flow

```
1. User installs package
   ├─> pip install my-conda-plugin
   └─> Package metadata includes entry_points

2. User runs conda
   ├─> Conda calls entry_points(group="conda")
   └─> Finds: my-plugin = "my_plugin.plugin"

3. Conda loads plugin
   ├─> import my_plugin.plugin
   └─> Scans for @hookimpl decorators

4. Conda registers hooks
   └─> Hooks are available to conda
```

## Best Practices

### 1. Unique Names

```python
# Good: Scoped and descriptive
entry_points={
    "conda": ["myorg-solver-plugin=myorg_conda.solver"],
}

# Bad: Generic, likely to conflict
entry_points={
    "conda": ["plugin=plugin"],
}
```

### 2. Lazy Loading

Entry points enable lazy loading - modules aren't imported until needed:

```python
# Only loads when actually used
for ep in entry_points(group="conda"):
    if ep.name == "my-plugin":
        plugin = ep.load()  # Import happens here
```

### 3. Error Handling

```python
for ep in entry_points(group="conda"):
    try:
        plugin = ep.load()
    except ImportError as e:
        print(f"Failed to load {ep.name}: {e}")
        continue
```

### 4. Versioning

```python
# Specify compatible versions
setup(
    name="my-plugin",
    install_requires=[
        "conda>=23.1.0",  # Requires plugin API
    ],
)
```

## Testing Entry Points

### Test Registration

```python
import pytest
from importlib.metadata import entry_points

def test_plugin_registered():
    """Verify entry point is registered."""
    eps = entry_points(group="conda")
    names = [ep.name for ep in eps]
    assert "my-plugin" in names

def test_plugin_loadable():
    """Verify entry point can be loaded."""
    eps = entry_points(group="conda")
    for ep in eps:
        if ep.name == "my-plugin":
            plugin = ep.load()
            assert plugin is not None
```

### Manual Testing

```bash
# Install in development mode
pip install -e .

# Check registration
python -c "
from importlib.metadata import entry_points
for ep in entry_points(group='conda'):
    if 'my' in ep.name:
        print(ep.name, '=', ep.value)
"

# Verify conda sees it
conda info --plugins
```

## Debugging

### Entry Point Not Found

**Problem**: Plugin not discovered

**Solutions**:
1. Reinstall package: `pip install -e .`
2. Check `pyproject.toml` syntax
3. Verify package is installed: `pip list | grep my-plugin`

### Import Error on Load

**Problem**: `ep.load()` fails

**Solutions**:
1. Check module path is correct
2. Verify dependencies are installed
3. Test import manually: `python -c "import my_plugin.plugin"`

### Wrong Entry Point Group

**Problem**: Using wrong group name

**Solution**: Verify the correct group:
- Conda plugins: `conda`
- Console scripts: `console_scripts`
- Pytest plugins: `pytest11`

## Entry Points vs Alternatives

| Method | Discovery | Flexibility | Standard |
|--------|-----------|-------------|----------|
| Entry Points | Automatic | High | Yes (PEP 566) |
| Manual Import | Manual | Low | N/A |
| Config Files | Semi-auto | Medium | No |

**Use entry points when**:
- Building plugin systems
- Creating CLI tools
- Integrating with frameworks
- Needing automatic discovery

## Examples in conda-lab

### Console Script

```toml
# recipes/hello-python/setup.py
entry_points={
    "console_scripts": [
        "hello-python=hello_python:main",
    ],
}
```

### Conda Plugin

```toml
# plugins/rebuilt-conda-graph/pyproject.toml
[project.entry-points.conda]
conda-graph-rebuilt = "conda_graph_rebuilt.plugin"
```

## References

- [PEP 566: Metadata for Python Packages 2.1](https://www.python.org/dev/peps/pep-0566/)
- [Setuptools: Entry Points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html)
- [Packaging Guide: Entry Points](https://packaging.python.org/en/latest/specifications/entry-points/)
- [importlib.metadata](https://docs.python.org/3/library/importlib.metadata.html)
