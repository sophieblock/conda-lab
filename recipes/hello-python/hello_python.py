"""A simple hello world Python package for conda recipe experimentation."""

__version__ = "1.0.0"


def greet(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: Name to greet
        
    Returns:
        Greeting message
    """
    return f"Hello, {name}! (from Python via conda)"


def main():
    """Main entry point for the hello-python CLI."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Simple hello world from Python"
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet"
    )
    
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
