# hello-python Recipe

A pure Python package demonstrating **noarch builds with entry points**.

## Single Concept

This recipe shows how to:
- Create a `noarch: python` package that works on any platform
- Use `script:` in meta.yaml instead of build.sh
- Define console entry points for CLI tools
- Package pure Python code with no compilation

## What's Included

- `hello_python.py`: Simple Python module with a CLI entry point
- `setup.py`: Standard Python packaging
- `meta.yaml`: Recipe with `noarch: python` and pip install script

## Key Points

**Noarch Build:**
```yaml
build:
  noarch: python
  script: {{ PYTHON }} -m pip install . -vv
```

`noarch: python` means this package works on any platform without rebuilding.

**Entry Points:**
```python
# In setup.py
entry_points={
    "console_scripts": [
        "hello-python=hello_python:main",
    ],
}
```

This creates a `hello-python` command that calls the `main()` function.

**No build.sh Needed:**
Simple Python packages use the `script:` field directly in meta.yaml.

## Building

```bash
conda activate conda-lab-build
conda build recipes/hello-python/
```

The output package is built once and works everywhere (hence "noarch").

## Output

Package location: `~/miniforge3/conda-bld/noarch/hello-python-1.0.0-*.tar.bz2`

## Testing

After installation:
```bash
hello-python World  # Prints: Hello, World! (from Python via conda)
hello-python --help  # Shows usage
```

## When to Use Noarch

Use `noarch: python` when your package:
- Has no compiled extensions
- Has no platform-specific code
- Works on Python ≥3.10 across all platforms

Do NOT use noarch if you need:
- Platform-specific dependencies
- Compiled C extensions
- Different behavior per platform
