---
applyTo: 'recipes/**/meta.yaml,recipes/**/build.sh,recipes/**/conda_build_config.yaml'
description: conda-build recipe best practices for macOS arm64
---

You are an expert in conda-build, conda-forge conventions, and macOS arm64 packaging.

## Recipe Structure

- Use clear, descriptive package names following conda-forge conventions
- Always specify exact version numbers in `package.version`
- Include comprehensive metadata: home, license, summary, description
- Provide source URLs with verified checksums (sha256)

## Dependencies

- Separate `host` dependencies (build-time) from `run` dependencies (runtime)
- Use version constraints appropriately: `>=1.0,<2` for semver packages
- Consider noarch: python when possible to reduce build matrix
- Always list compiler packages explicitly in host for compiled code

## Build Scripts (macOS arm64)

- Start bash scripts with `#!/bin/bash` and `set -euxo pipefail`
- Set MACOSX_DEPLOYMENT_TARGET appropriately (11.0+ for arm64)
- Use `${PREFIX}` environment variable, never hardcode paths
- For Python packages, prefer `python -m pip install . -vv --no-deps --no-build-isolation`
- Test that compiled extensions load correctly in the test section

## Platform Targeting

- Specify `osx` and `arm64` in build requirements when targeting macOS arm64
- Use `skip: true` selectively with clear comments explaining why
- Consider cross-compilation constraints
- Test on actual arm64 hardware when possible

## Variants

- Define variants in `conda_build_config.yaml` at recipe root or globally
- Use pin_subpackage for internal package dependencies
- Keep variant matrices small to reduce build time
- Document variant rationale in comments

## Testing

- Include imports test for Python packages: `imports: [package_name]`
- Add command-line tests for executables: `commands: [package --version]`
- Consider requires: section for test-only dependencies
- Verify cross-platform behavior when claiming noarch

## Security & Reproducibility

- Always verify source checksums
- Pin build numbers when rebuilding without version changes
- Use specific commit SHAs for git sources when possible
- Document any patches applied to upstream source

## Common macOS arm64 Issues

- Some packages may need `ARCHFLAGS="-arch arm64"` set
- Rosetta emulation can mask arm64-specific build issues
- Check for hardcoded x86_64 assumptions in build scripts
- Verify shared library architectures with `file` or `lipo`
