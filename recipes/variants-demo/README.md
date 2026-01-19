# variants-demo Recipe

A Python package demonstrating **conda-build variant matrices**.

## Single Concept

This recipe shows how to:
- Define build variants in `conda_build_config.yaml`
- Create a matrix of Python versions, NumPy versions, and custom variants
- Customize build strings to identify each variant
- Use variant variables in requirements

## What's Included

- `variants_demo.py`: Python module that reports build configuration
- `setup.py`: Standard Python packaging with NumPy dependency
- `meta.yaml`: Recipe using variant variables
- `conda_build_config.yaml`: Variant matrix definition

## Key Points

**Variant Configuration:**
```yaml
# conda_build_config.yaml
python:
  - 3.10
  - 3.11

numpy:
  - 1.24
  - 1.26

variant_name:
  - standard
  - optimized
```

This creates **8 total builds** (2 Python × 2 NumPy × 2 custom = 8).

**Using Variants in Recipe:**
```yaml
requirements:
  run:
    - python
    - numpy {{ numpy }}

build:
  string: py{{ py }}_{{ variant_name }}_{{ PKG_BUILDNUM }}
```

**Zip Keys:**
The `zip_keys` section controls how variants combine:
```yaml
zip_keys:
  - python
  - numpy
```

With zip_keys, you get **paired** builds instead of full cross-product:
- Python 3.10 + NumPy 1.24
- Python 3.11 + NumPy 1.26

Without zip_keys, you'd get all 4 combinations (2×2).

## Building

### Render to see all variants:
```bash
conda activate conda-lab-build
conda render recipes/variants-demo/
```

### Build all variants:
```bash
conda build recipes/variants-demo/
```

### Build specific variant:
```bash
conda build recipes/variants-demo/ --variants '{"python": "3.11", "numpy": "1.26"}'
```

## Output

Each variant produces a separate package:
- `variants-demo-0.1.0-py310_standard_0.tar.bz2`
- `variants-demo-0.1.0-py310_optimized_0.tar.bz2`
- `variants-demo-0.1.0-py311_standard_0.tar.bz2`
- `variants-demo-0.1.0-py311_optimized_0.tar.bz2`

## Testing

After installation:
```bash
variants-demo --info
```

Shows which Python, NumPy, and platform the package was built with.

## When to Use Variants

Use variants when you need to:
- Support multiple Python or NumPy versions
- Build against different dependency versions
- Create optimized vs standard builds
- Match user environment constraints

Avoid variants for:
- Pure noarch Python packages (use `noarch: python` instead)
- Single-version dependencies
- Packages with no version sensitivity
