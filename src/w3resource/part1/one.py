"""
Docstring para w3resource.part1.main

This is a firt part for w3resource in python basic 1-50
Python Basic (Part -I) - Exercises, Practice, Solution

Name: Hector Daivd Leiva Gamboa
Start: 01-13-2026 (MM/DD/YYYY)
End:
Version: Python3.13
"""

import sys
import datetime
import math

def formatted_twinkle_poem():
    #\n it's a next line command
    #\t it's a tabular command
    print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

def python_version_checker():
    # Print the Python version to the console
    print("Python version")

    # Use the sys.version attribute to get the Python version and print it
    print(sys.version)

    # Print information about the Python version
    print("Version info.")

    # Use the sys.version_info attribute to get detailed version information and print it
    print(sys.version_info)

def current_dateTime_display():
    #datetime it's a library the python
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def circle_area_calculator():
    r = float(input("Enter your radius: "))
    print(f"r = {r}")
    print(f"Area = {math.pi*r**2}")

def reverse_full_name():
    fname = input("What is your name: ")
    lname = input("What is your last name: ")

    print(f"Hello {lname} {fname}")

def list_and_tuple_generator():
    numbers = input("List numbers: ")  # ej: 3, 2, 1, 23
    list = numbers.split(",")
    tupla = tuple(list)

    print(list)
    print(tupla)