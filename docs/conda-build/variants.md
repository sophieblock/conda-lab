# Conda Build Variants

Variants allow building multiple versions of the same package with different dependencies or configurations.

## What Are Variants?

Variants create a build matrix from `conda_build_config.yaml`:

```yaml
# conda_build_config.yaml
python:
  - 3.10
  - 3.10
  - 3.11

numpy:
  - 1.24
  - 1.26
```

This creates **6 builds** (3 Python × 2 NumPy):
- `mypackage-1.0-py39_numpy124_0.tar.bz2`
- `mypackage-1.0-py39_numpy126_0.tar.bz2`
- `mypackage-1.0-py310_numpy124_0.tar.bz2`
- `mypackage-1.0-py310_numpy126_0.tar.bz2`
- `mypackage-1.0-py311_numpy124_0.tar.bz2`
- `mypackage-1.0-py311_numpy126_0.tar.bz2`

## Basic Usage

### In meta.yaml

Reference variant variables with Jinja2:

```yaml
requirements:
  host:
    - python {{ python }}
    - numpy {{ numpy }}
  run:
    - python
    - numpy
```

### Build String

Customize the build identifier:

```yaml
build:
  string: py{{ py }}_np{{ numpy | replace(".", "") }}_{{ PKG_BUILDNUM }}
```

## Variant Configuration

### Global Config

System-wide: `~/miniforge3/conda_build_config.yaml`

```yaml
# All recipes use these by default
python:
  - 3.10
  - 3.10
  - 3.11
```

### Recipe-Specific Config

In recipe directory: `recipes/mypackage/conda_build_config.yaml`

```yaml
# Only for this recipe
python:
  - 3.11  # Override: only build for Python 3.11

custom_variant:
  - option_a
  - option_b
```

## Advanced Features

### Zipping Variants

Build only specific combinations:

```yaml
python:
  - 3.10
  - 3.10

numpy:
  - 1.24
  - 1.26

zip_keys:
  - python
  - numpy
```

Result: **2 builds** instead of 4:
- Python 3.10 + NumPy 1.24
- Python 3.10 + NumPy 1.26

### Pin Run Exports

Control runtime dependencies:

```yaml
pin_run_as_build:
  python:
    min_pin: x.x    # e.g., >=3.10,<3.10
    max_pin: x.x
  numpy:
    min_pin: x.x
    max_pin: x
```

### Custom Variants

Add your own variant dimensions:

```yaml
# conda_build_config.yaml
variant_name:
  - standard
  - optimized

blas_impl:
  - openblas
  - mkl
```

Use in meta.yaml:

```yaml
build:
  string: {{ variant_name }}_{{ blas_impl }}_{{ PKG_BUILDNUM }}

requirements:
  run:
    - blas * {{ blas_impl }}  # [blas_impl != 'standard']
```

## Viewing Variants

### List All Variants

```bash
conda render recipes/mypackage/ --variants
```

Output:
```
python=3.10, numpy=1.24
python=3.10, numpy=1.26
python=3.10, numpy=1.24
...
```

### Render Specific Variant

```bash
conda render recipes/mypackage/ --variants '{"python": "3.11", "numpy": "1.26"}'
```

## Build Matrix Example

See `recipes/variants-demo/` for a complete example:

```bash
# Render all variants
conda render recipes/variants-demo/

# Build all variants
conda build recipes/variants-demo/

# Build specific variant
conda build recipes/variants-demo/ --variants '{"python": "3.11"}'
```

## Common Patterns

### Python-Only Variants

```yaml
python:
  - 3.10
  - 3.10
  - 3.11

# In meta.yaml
build:
  noarch: python  # Skip variants entirely for pure Python
```

### Platform-Specific Variants

```yaml
# Only on macOS
c_compiler:  # [osx]
  - clang    # [osx]

# Only on Linux
c_compiler:  # [linux]
  - gcc      # [linux]
```

### Optional Dependencies

```yaml
variant_type:
  - minimal
  - full

# In meta.yaml
requirements:
  run:
    - core_dep
    - optional_dep  # [variant_type == 'full']
```

## Performance Tips

1. **Use `noarch: python`** when possible (no variants needed)
2. **Limit variant combinations** with `zip_keys`
3. **Skip unnecessary platforms** with selectors
4. **Test locally** before building all variants

## Debugging

### Check Rendered Output

```bash
conda render recipes/mypackage/ --file rendered.yaml
cat rendered.yaml
```

### Build One Variant

```bash
conda build recipes/mypackage/ --variants '{"python": "3.11"}'
```

### Inspect Build String

The build string encodes the variant:

```
package-1.0-py311h1234567_0.tar.bz2
            ^^^^^          ^
            variant        build number
```

## References

- [conda-build: Build Variants](https://docs.conda.io/projects/conda-build/en/latest/resources/variants.html)
- [conda_build_config.yaml reference](https://docs.conda.io/projects/conda-build/en/latest/resources/build-scripts.html#conda-build-config-yaml)
- [Example: NumPy variants in conda-forge](https://github.com/conda-forge/numpy-feedstock)
