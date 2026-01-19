# macOS Environment Variables in conda-build

Understanding environment variables is critical for debugging conda-build issues on macOS, especially arm64.

## Key Build Variables

### Compiler Variables

```bash
# C Compiler
CC=clang                    # Set by conda-build
CFLAGS=-arch arm64         # Architecture flags

# C++ Compiler  
CXX=clang++
CXXFLAGS=-arch arm64

# Linker
LDFLAGS=-Wl,-pie          # Position independent executable
```

### macOS SDK Variables

```bash
CONDA_BUILD_SYSROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk
MACOSX_DEPLOYMENT_TARGET=11.0  # Minimum macOS version
OSX_ARCH=arm64
```

### Build Directories

```bash
PREFIX=$CONDA_PREFIX/envs/my-build  # Install destination
BUILD_PREFIX=$PREFIX                 # Build-time tools
SRC_DIR=/tmp/conda-bld/.../work     # Source extraction
```

### Python Variables

```bash
PYTHON=$PREFIX/bin/python
PY_VER=3.11
PY3=1
```

## Debugging Tips

### Print All Variables

Add to `build.sh`:

```bash
env | sort
```

### Check Compiler

```bash
echo "CC: $CC"
echo "CXX: $CXX"
$CC --version
```

### Verify Architecture

```bash
file $PREFIX/bin/my-program
# Should show: Mach-O 64-bit executable arm64
```

## Common Issues

### Wrong Architecture

**Problem**: Binary built for x86_64 instead of arm64

**Solution**: Ensure `CFLAGS` and `CXXFLAGS` include `-arch arm64`

### SDK Not Found

**Problem**: Can't find macOS SDK headers

**Solution**: Install Xcode Command Line Tools:
```bash
xcode-select --install
```

### Deployment Target

**Problem**: Binary requires newer macOS than expected

**Solution**: Set `MACOSX_DEPLOYMENT_TARGET` explicitly in recipe

## References

- [conda-build docs: Environment Variables](https://docs.conda.io/projects/conda-build/en/latest/user-guide/environment-variables.html)
- [Apple: Building from Command Line](https://developer.apple.com/library/archive/technotes/tn2339/)
