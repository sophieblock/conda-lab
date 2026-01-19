# Render vs Build vs Test in conda-build

Understanding the three phases of conda-build is essential for debugging recipes.

## Overview

```
meta.yaml → RENDER → rendered recipe → BUILD → package.tar.bz2 → TEST → validation
```

## 1. Render Phase

**Purpose**: Process Jinja2 templates and selectors to produce a concrete recipe

**What Happens**:
- Jinja2 variables (`{{ name }}`, `{{ version }}`) are evaluated
- Selectors (`# [osx]`) are processed
- `conda_build_config.yaml` variants are applied
- Output: A plain YAML recipe (no templates)

**Command**:
```bash
conda render recipes/hello-python/
```

**When to Use**:
- Debugging template syntax errors
- Understanding how variants expand
- Checking which selectors are active

**Example**:

Input:
```yaml
{% set version = "1.0.0" %}
package:
  name: hello
  version: {{ version }}
  
requirements:
  build:
    - gcc  # [linux]
    - clang  # [osx]
```

Rendered (on macOS):
```yaml
package:
  name: hello
  version: 1.0.0
  
requirements:
  build:
    - clang
```

## 2. Build Phase

**Purpose**: Create the actual conda package

**What Happens**:
- Source is fetched/extracted
- Build script (`build.sh` or `build.py`) runs
- Files are collected into `$PREFIX`
- Package metadata is generated
- `.tar.bz2` archive is created

**Command**:
```bash
conda build recipes/hello-python/
```

**When to Use**:
- Creating packages for distribution
- Testing the full build process
- Debugging build script errors

**Output Location**:
```
~/miniforge3/conda-bld/osx-arm64/hello-python-1.0.0-py311_0.tar.bz2
```

## 3. Test Phase

**Purpose**: Validate the built package works correctly

**What Happens**:
- Package is installed in a clean environment
- Test imports are verified
- Test commands are executed
- Test files are run (if specified)

**Automatic**: Runs after build by default

**Command** (standalone):
```bash
conda build --test package.tar.bz2
```

**When to Use**:
- Verifying package functionality
- Re-testing without rebuilding
- Debugging test failures

**What's Tested**:
```yaml
test:
  imports:           # Python imports work
    - my_module
  commands:          # CLI commands work
    - my-tool --help
  requires:          # Extra test dependencies
    - pytest
  source_files:      # Copy files for testing
    - tests/
```

## Quick Reference

| Phase  | Input            | Output              | Jinja2? | Build Script? |
|--------|------------------|---------------------|---------|---------------|
| Render | meta.yaml        | Rendered recipe     | Yes     | No            |
| Build  | Rendered recipe  | .tar.bz2 package    | No      | Yes           |
| Test   | .tar.bz2 package | Pass/Fail           | No      | No            |

## Common Workflows

### Debug Template Issues
```bash
conda render recipes/my-package/
```

### Build Without Testing
```bash
conda build --no-test recipes/my-package/
```

### Test Without Building
```bash
conda build --test ~/miniforge3/conda-bld/osx-arm64/my-package-*.tar.bz2
```

### Build + Test (default)
```bash
conda build recipes/my-package/
```

## Troubleshooting

### Render Fails
- Check Jinja2 syntax
- Verify `conda_build_config.yaml` format
- Look for undefined variables

### Build Fails
- Check `build.sh` script
- Verify environment variables
- Check compiler output

### Test Fails
- Check imports in clean environment
- Verify commands are in PATH
- Check test requirements installed

## References

- [conda-build concepts](https://docs.conda.io/projects/conda-build/en/latest/concepts/index.html)
- [Recipe meta.yaml](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html)
