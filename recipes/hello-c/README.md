# hello-c Recipe

A minimal C program demonstrating **native compilation with conda-build**.

## Single Concept

This recipe shows how to:
- Use `{{ compiler('c') }}` to get platform-appropriate C compiler
- Build a native executable with `build.sh`
- Target specific platforms with selectors (`# [osx and arm64]`)

## What's Included

- `hello.c`: Simple C program
- `build.sh`: Build script that uses `$CC`, `$CFLAGS`, `$LDFLAGS`
- `meta.yaml`: Recipe with compiler dependency

## Key Points

**Compiler Selection:**
```yaml
requirements:
  build:
    - {{ compiler('c') }}
```

On macOS arm64, this resolves to `clang_osx-arm64`.

**Platform Selector:**
```yaml
build:
  skip: True  # [not osx or not arm64]
```

This prevents builds on non-macOS or non-arm64 platforms.

**Build Script:**
The `build.sh` uses conda-provided environment variables:
- `$CC`: C compiler path
- `$CFLAGS`: Compiler flags (including `-arch arm64`)
- `$LDFLAGS`: Linker flags
- `$PREFIX`: Installation directory

## Building

```bash
conda activate conda-lab-build
conda build recipes/hello-c/
```

## Output

The built package contains a single executable at `$PREFIX/bin/hello-c`.

## Testing

After installation:
```bash
hello-c  # Prints: Hello from C on macOS arm64!
```

The test section in `meta.yaml` verifies the command exists and runs.
