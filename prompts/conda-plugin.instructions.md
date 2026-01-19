---
applyTo: 'plugins/**/pyproject.toml,plugins/**/src/**/*.py'
description: conda plugin development best practices
---

You are an expert in conda plugin architecture and Python packaging with pyproject.toml.

## Plugin Structure

- Use modern src/ layout: `src/{plugin_name}/`
- Define entry points in `[project.entry-points."conda"]` section
- One plugin can provide multiple hooks via separate entry points
- Name entry points descriptively: `my_plugin_solver`, `my_plugin_reporter`

## Entry Point Configuration

```toml
[project.entry-points."conda"]
solver = "my_plugin.hooks:get_solver"
subcommands = "my_plugin.hooks:get_subcommands"
```

- Entry point values must be `module.path:function_name` format
- Functions must follow conda plugin hook signatures
- Register in correct category: `conda`, `conda.solvers`, `conda.subcommands`

## Hook Implementation

**Available Hooks:**
- `CondaSubcommand` - Register new `conda` CLI subcommands
- `CondaSolver` - Register custom dependency solvers
- `CondaVirtualPackage` - Define virtual packages
- `CondaPreCommand`/`CondaPostCommand` - Execute around conda commands

**Hook Requirements:**
- Return correct type: `CondaSubcommand` instance, solver name, etc.
- Handle errors gracefully with proper logging
- Don't assume specific conda versions without version checks
- Follow conda's logging patterns using `logging.getLogger(__name__)`

## Plugin Discovery

- Plugins auto-discovered when installed in conda's environment
- Test discovery with: `conda info --all` (shows loaded plugins)
- Debug loading issues by checking entry point registration
- Ensure plugin package is installed in same env as conda

## Testing Strategy

- Unit test hook functions independently
- Integration test plugin loading via `conda` CLI
- Test in isolated conda environment
- Verify entry points with: `python -c "import importlib.metadata; print(importlib.metadata.entry_points(group='conda'))"`

## Dependencies

- Minimize dependencies; conda and stdlib preferred
- If external deps needed, ensure conda-installable
- Don't depend on conda internals unless necessary (they may change)
- Specify `requires-python` constraint in pyproject.toml

## Documentation

- Include docstrings for all public functions
- Document hook return types explicitly
- Provide usage examples in README.md
- Explain when/why someone would use your plugin

## Packaging Best Practices

- Use semantic versioning
- Include license file (Apache-2.0, MIT, etc.)
- Set `dynamic = ["version"]` with version from git tags or package
- Build with: `python -m build`
- Test install with: `pip install -e .` for development
