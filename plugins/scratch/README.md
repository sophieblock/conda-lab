# Plugin Scratch Space

This directory is for experimental plugin code, prototypes, and quick tests.

## Purpose

Use this space to:
- Sketch out new plugin ideas
- Test plugin APIs without full structure
- Keep experimental code separate from production plugins
- Document failed experiments and learnings

## Examples

```python
# Quick test of a plugin hook
from conda import plugins

@plugins.hookimpl
def conda_subcommands():
    yield plugins.CondaSubcommand(
        name="test",
        summary="Test command",
        action=lambda args: print("Testing!"),
    )
```

## Convention

- Keep files prefixed with purpose: `test_*.py`, `experiment_*.py`, `scratch_*.py`
- Add comments explaining what you're testing
- Don't commit this folder to production plugins
