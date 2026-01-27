"""
Docstring para leetcode.main
"""

from src.fuction import *
from src.clases import *

def main():
    #Clase que tiene todas las soluciones
    s = Solution() 

    try:
        print(s.addTwoNumbers())
    except ValueError as e:
        print(f"Error: {e}")

    two()


if __name__ == "__main__":
    main()