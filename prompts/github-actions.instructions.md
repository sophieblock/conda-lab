---
applyTo: '.github/**/*.yml,.github/**/*.yaml'
description: GitHub Actions best practices for conda-build CI/CD
---

You are an expert in DevOps, CI/CD, GitHub Actions, and conda-build automation.

## Conda-Specific Workflow Patterns

### Setup Conda/Mamba

- Use `conda-incubator/setup-miniconda@v3` for conda environments
- Pin to specific action version SHA when possible
- Prefer `mamba` or `micromamba` for faster dependency resolution
- Cache conda environments using `actions/cache` with conda env hash

```yaml
- uses: conda-incubator/setup-miniconda@v3
  with:
    mamba-version: "*"
    channels: conda-forge
    activate-environment: build-env
    environment-file: envs/build.yml
    auto-activate-base: false
```

### Building Conda Packages

- Run `conda-build` in a dedicated job
- Set `CONDA_BLD_PATH` to control output location
- Upload built packages as artifacts with short retention
- Test on matrix of platforms: `[macos-latest, macos-14]` for intel/arm64

```yaml
strategy:
  matrix:
    os: [macos-14]  # arm64
    python-version: ['3.9', '3.10', '3.11']
```

### Testing Recipes

- Create fresh test environment from built package
- Don't test in build environment (contaminated)
- Use `conda install --use-local` to test local builds
- Verify imports and run command-line tests

## Security Best Practices

- Always set `permissions: contents: read` at workflow level
- Use `permissions: write` only for jobs that need it
- Pin actions to commit SHA: `actions/checkout@abc123...`
- Never print conda auth tokens or secrets in logs
- Use OIDC for cloud uploads instead of static tokens

## Performance & Caching

- Cache conda packages: `~/.conda/pkgs` and `~/conda_pkgs_dir`
- Cache pip packages: `~/.cache/pip`
- Use cache key based on environment file hash
- Set appropriate `cache-hit` conditions to skip setup

```yaml
- uses: actions/cache@v4
  with:
    path: ~/conda_pkgs_dir
    key: ${{ runner.os }}-conda-${{ hashFiles('envs/build.yml') }}
```

## Platform-Specific Considerations

### macOS Runners
- `macos-14` for arm64 (Apple Silicon)
- `macos-latest` for x86_64 (Intel) - currently macos-14
- Set `MACOSX_DEPLOYMENT_TARGET=11.0` for arm64 builds
- Homebrew pre-installed but may conflict with conda

### Matrix Builds
- Test across Python versions: 3.9, 3.10, 3.11, 3.12
- Test noarch packages once, skip matrix
- Use `fail-fast: false` to see all platform failures
- Set reasonable `timeout-minutes` (30-60 for conda-build)

## Workflow Organization

### Job Structure
1. **validate** - Lint recipes with `conda-build --check`
2. **build** - Build packages with `conda-build`
3. **test** - Install and test in clean environment
4. **upload** - Upload artifacts or publish to channel

### Triggers
- Build on: `push` to main, `pull_request`
- Use `paths:` filter for recipe changes only
- Set `concurrency` group to cancel outdated PR builds

```yaml
on:
  push:
    branches: [main]
    paths:
      - 'recipes/**'
      - 'envs/*.yml'
  pull_request:
    paths:
      - 'recipes/**'

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## Best Practices

- Keep workflows focused: one workflow per logical task
- Move complex logic to shell scripts in repo
- Use `defaults.run.shell: bash -l {0}` for conda activation
- Set explicit `working-directory` when needed
- Use meaningful job and step names
- Add comments explaining non-obvious conda commands
