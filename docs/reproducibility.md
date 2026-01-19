# Reproducibility in Conda Environments

Strategies for creating reproducible conda environments across machines and time.

## The Reproducibility Challenge

Conda environments can drift due to:
- Package updates in channels
- Platform differences (x86_64 vs arm64)
- Solver decisions changing over time
- Implicit dependencies resolved differently

## Levels of Reproducibility

### Level 1: Loose (environment.yml)

**File**: `environment.yml`

```yaml
name: myenv
channels:
  - conda-forge
dependencies:
  - python=3.11
  - numpy
  - pandas
```

**Pros**: Flexible, gets latest compatible versions  
**Cons**: Non-deterministic, may break over time

### Level 2: Pinned (environment.yml with versions)

```yaml
name: myenv
channels:
  - conda-forge
dependencies:
  - python=3.11.5
  - numpy=1.26.0
  - pandas=2.1.1
```

**Pros**: More stable  
**Cons**: Still resolves dependencies, platform-specific

### Level 3: Explicit (conda list --explicit)

**Command**:
```bash
conda list --explicit > spec-file.txt
```

**Output** (`spec-file.txt`):
```
# This file may be used to create an environment using:
# $ conda create --name myenv --file spec-file.txt
# platform: osx-arm64
@EXPLICIT
https://conda.anaconda.org/conda-forge/osx-arm64/python-3.11.5-h47c9636_0.tar.bz2#abc123...
https://conda.anaconda.org/conda-forge/osx-arm64/numpy-1.26.0-py311h1234567_0.tar.bz2#def456...
```

**Pros**: Fully deterministic, exact URLs with hashes  
**Cons**: Platform-specific, URLs may become unavailable

### Level 4: Locked (conda-lock)

**Tool**: [conda-lock](https://github.com/conda/conda-lock)

```bash
conda-lock --file environment.yml --platform osx-arm64
```

**Output**: `conda-lock.yml` with exact versions and hashes for multiple platforms

**Pros**: Cross-platform, deterministic, maintainable  
**Cons**: Requires external tool

## Best Practices

### 1. Pin Direct Dependencies

```yaml
dependencies:
  # Pin direct dependencies
  - python=3.11.*
  - numpy>=1.24,<2.0
  - pandas~=2.1.0
  
  # Let conda resolve transitive deps
```

### 2. Use conda-forge Consistently

```yaml
channels:
  - conda-forge  # Consistent package builds
  - defaults     # Avoid mixing if possible
```

### 3. Document Platform

```yaml
# environment.yml
# Platform: macOS arm64 (Apple Silicon)
# Created: 2024-01-15
name: myenv
```

### 4. Lock for Production

```bash
# Development: use environment.yml
conda env create -f environment.yml

# Production: generate and use lock file
conda-lock --file environment.yml
conda env create -f conda-lock.yml
```

### 5. Version Control

```bash
# Commit both files
git add environment.yml
git add conda-linux-64.lock  # or conda-lock.yml
```

## Workflow Patterns

### Pattern A: Single Platform

```bash
# 1. Create environment
conda env create -f environment.yml

# 2. Export exact state
conda env export > environment.lock.yml

# 3. Recreate exactly
conda env create -f environment.lock.yml
```

### Pattern B: Multi-Platform

```bash
# 1. Create lock files for all platforms
conda-lock --file environment.yml \
  --platform osx-arm64 \
  --platform osx-64 \
  --platform linux-64

# 2. Use platform-specific lock
conda env create -f conda-osx-arm64.lock
```

### Pattern C: Docker

```dockerfile
FROM continuumio/miniconda3

# Copy lock file
COPY conda-linux-64.lock /tmp/

# Create environment from lock
RUN conda create --name myenv --file /tmp/conda-linux-64.lock
```

## Testing Reproducibility

### Test Script

```bash
#!/bin/bash
# test-reproducibility.sh

ENV_NAME="test-repro"

# Clean slate
conda env remove -n $ENV_NAME -y

# Create from spec
conda env create -n $ENV_NAME -f environment.yml

# Activate and test
conda activate $ENV_NAME
python -c "import numpy; print(numpy.__version__)"

# Export and compare
conda env export > test-export.yml
diff environment.yml test-export.yml
```

### Continuous Integration

```yaml
# .github/workflows/test-env.yml
name: Test Environment
on: [push]
jobs:
  test:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v3
      - uses: conda-incubator/setup-miniconda@v2
        with:
          environment-file: environment.yml
      - run: |
          conda list
          python -c "import numpy; print('OK')"
```

## Handling Drift

### Problem: Environment Won't Recreate

```bash
# Error: Package not available
ResolvePackageNotFound: numpy=1.26.0
```

**Solutions**:

1. **Relax pins**: Update `environment.yml` with newer versions
2. **Use conda-forge**: More persistent package availability
3. **Archive packages**: Keep local mirror

### Problem: Different Behavior on Different Machines

**Solutions**:

1. Use explicit spec file (`conda list --explicit`)
2. Check for platform-specific packages
3. Verify architecture matches (arm64 vs x86_64)

### Problem: CI/CD Environment Different

**Solutions**:

1. Use conda-lock for determinism
2. Match runner platform to target
3. Cache conda packages in CI

## Advanced: Custom Channels

### Local Package Cache

```bash
# Download packages
conda create -n myenv --download-only numpy pandas

# Packages cached in: ~/miniforge3/pkgs/

# Create offline
conda create -n myenv --offline numpy pandas
```

### Private Channel

```bash
# Create channel directory
mkdir -p ~/my-channel/osx-arm64

# Copy packages
cp ~/miniforge3/pkgs/*.tar.bz2 ~/my-channel/osx-arm64/

# Index channel
conda index ~/my-channel

# Use channel
conda create -n myenv -c file://~/my-channel numpy
```

## Checklist for Reproducibility

- [ ] Pin Python version explicitly
- [ ] Pin major versions of key dependencies
- [ ] Use consistent channel priority
- [ ] Document target platform
- [ ] Generate lock file for production
- [ ] Test recreation from scratch
- [ ] Version control environment files
- [ ] Use conda-lock for multi-platform
- [ ] Archive critical packages locally
- [ ] Automate environment testing in CI

## Tools

| Tool | Purpose | Best For |
|------|---------|----------|
| `conda env export` | Export current env | Quick snapshots |
| `conda list --explicit` | Explicit URLs | Exact recreation |
| `conda-lock` | Multi-platform locks | Production deployments |
| `mamba` | Fast solver | Large environments |

## macOS arm64 Specifics

### Architecture Issues

```bash
# Check if running under Rosetta
uname -m  # Should show "arm64" not "x86_64"

# Ensure arm64 packages
conda config --env --set subdir osx-arm64
```

### Miniforge vs Anaconda

```bash
# Miniforge: Native arm64 support
# Better for macOS arm64 reproducibility
brew install miniforge

# Anaconda: x86_64 by default
# Requires Rosetta emulation
```

## References

- [Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [conda-lock Documentation](https://conda.github.io/conda-lock/)
- [Conda-Forge Best Practices](https://conda-forge.org/docs/maintainer/knowledge_base.html)
- [Miniforge](https://github.com/conda-forge/miniforge)

## See Also

- `envs/dev.yml` - Example development environment
- `envs/build.yml` - Example build environment
