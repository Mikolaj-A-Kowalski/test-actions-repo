"""
Command-line interface for the hello world package.
"""

import argparse
import sys
from typing import List, Optional

from .core import greet, farewell


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the command-line interface.
    
    Args:
        argv: Command line arguments. If None, uses sys.argv.
    
    Returns:
        int: Exit code (0 for success, non-zero for error).
    """
    parser = argparse.ArgumentParser(
        description="A simple hello world program",
        prog="hello-world"
    )
    
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet (default: World)"
    )
    
    parser.add_argument(
        "--farewell",
        action="store_true",
        help="Say goodbye instead of hello"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    
    if argv is None:
        argv = sys.argv[1:]
    
    try:
        args = parser.parse_args(argv)
        
        if args.farewell:
            message = farewell(args.name)
        else:
            message = greet(args.name)
        
        print(message)
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
