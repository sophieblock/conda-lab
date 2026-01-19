"""Variants demo package showing conda-build variant matrices."""

import sys
import platform

__version__ = "0.1.0"


def get_build_info():
    """Return information about the build environment."""
    try:
        import numpy
        numpy_version = numpy.__version__
    except ImportError:
        numpy_version = "not installed"
    
    return {
        "python_version": sys.version.split()[0],
        "platform": platform.platform(),
        "machine": platform.machine(),
        "numpy_version": numpy_version,
    }


def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Variants demo package"
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show build information"
    )
    
    args = parser.parse_args()
    
    if args.info:
        info = get_build_info()
        print("Build Information:")
        for key, value in info.items():
            print(f"  {key}: {value}")
    else:
        print(f"variants-demo v{__version__}")
        print("Use --info to see build details")


if __name__ == "__main__":
    main()
