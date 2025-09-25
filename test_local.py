#!/usr/bin/env python3
"""
Local development script to test the package.
"""

from hello_world import greet
from hello_world.core import farewell

if __name__ == "__main__":
    print("Testing the hello_world package:")
    print(greet())
    print(greet("Python"))
    print(farewell())
    print(farewell("Development"))
