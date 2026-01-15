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
import calendar

def two():
    string = input("Enter the name fuction: ")
    print(string.replace(" ", "_").lower())

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

def list_and_tuple_generator1():
    numbers = input("List numbers: ")  # ej: 3, 2, 1, 23
    numbers=numbers.replace(" ", "")
    list = numbers.split(",")
    tupla = tuple(list)

    print(list)
    print(tupla)

def list_and_tuple_generator2():
    numbers = input("List numbers: ")  # ej: 3, 2, 1, 23
    newString = ""
    newList = []
    newTupla = ()

    for ch in numbers:
        if ch.isdigit():
            newString+=ch
        elif ch in ",":
            if newString != "":
                newList.append(newString)
                newString = ""

    if newString != "":
        newList.append(newString)

    print(newList)
    newTupla = tuple(newList)
    print(newTupla)

def file_extension_extractor():
    string = input("Enter your filename: ")
    newString = ""
    flag = False

    for ch in string:

        if flag:
            newString += ch

        if ch in ".":
            flag = True

    print(newString)

def first_and_last_colors():
    color_list = ["Red","Green","White" ,"Black", "Yellow"]

    print(color_list[0])
    print(color_list[len(color_list)-1])

def exam_schedule_formatter():
    exam_st_date = (11, 12, 2014)
    print(f"The examination will start from: {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")

def number_expansion_calculator():
    n = int(input("Enter a number: "))
    n = n + n*11 + n*111
    print(n)

def function_documentation_printer():
    print("---abs---")
    print(abs.__doc__)

    print("---len---")
    print(len.__doc__)

    print("---input---")
    print(input.__doc__)

    print("---int---")
    print(int.__doc__)

def monthly_calendar_display():
    calendario = calendar

    y = int(input("Input the year: "))
    m = int(input("Input the month: "))

    print(calendario.month(y,m))

def multiline_here_document():
    print("""        a string that you "don't" have to escape
        This
        is a ....... multi-line
        heredoc string --------> example""")

def days_between_dates():
    day1 = (2014, 7, 2)
    day2 = (2014, 7, 11)

    day1 = datetime.date(day1[0], day1[1], day1[2])
    day2 = datetime.date(day2[0], day2[1], day2[2])

    print(abs(day2-day1))

def sphere_volume_calculator():
    r = 6
    print(f"{(4/3) * r**3}π")




