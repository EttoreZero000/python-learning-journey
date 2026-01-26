"""
Docstring para leetcode.main
"""

from src.fuction import *

def main():
    try:
        print(one())
    except ValueError as e:
        print(f"Error: {e}")

    two()


if __name__ == "__main__":
    main()