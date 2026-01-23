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
from math import *
import calendar
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

def two():
    string = input("Enter the name fuction: ")
    print(string.replace(" ", "_").lower())

def formatted_twinkle_poem():
    #\n it's a next line command
    #\t it's a tabular command
    print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
#1^^^^^^^^^^^^^^

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
#10^^^^^^^^^^

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

def difference_from_17():
    n = int(input("Enter a number: "))

    if n < 17: 
        print(17-n)
    else:
        print((n-17)*2)

def number_range_tester():
    n = int(input("Enter a number: "))

    if 100 < n and n < 2000:
        print(f"Yes, {n} is whether of 100 to 2000")
        return

    print(f"No, {n} is not whether of 100 to 2000")

def triple_sum_calculator():
    n1 = int(input("Enter the number: "))
    n2 = int(input("Enter the number: "))
    n3 = int(input("Enter the number: "))

    if n1 == n2 == n3:
        print(f"Output: {n1*3}")
        return
    print(f"Output: {n1+n2+n3}")

def prefix_is_string_modifier():
    n = input("Enter the string: ")

    if n[0].lower()+n[1].lower() in "is":
        print(n)
        return
    
    print(f"Is {n}")

def string_copy_generator():
    n = input("Enter the string: ")
    c = int(input("Enter the integer for copy: "))

    
    print(n*c)
#20 ^^^^^^^^^^^^
def even_or_odd_checker():
    n = int(input("Enter the number: "))

    if n % 2 == 0:
        print(f"The number {n} is even")
        return
    print(f"The number {n} is odd")

def count_4_in_list():
    list = [1,4,6,7,4,4,4]
    x = 0
    for n in list:
        if n == 4:
            x+=1
    print(x)

def string_prefix_copies():
    string = input("Enter the string: ")
    n = int(input("Enter the integer: "))

    if len(string) < 2:
        print((string[0])*n)
        return
        
    print((string[0]+string[1])*n)

def vowel_tester():
    n = input("Enter the char: ")

    if len(n)>1 or n=="":
        raise ValueError("I don't can, one letter")

    if n in "aeiou":
        return True
    return False

def value_in_group_tester():
    list = [1,2,3,5]
    n = input("Enter the int: ")

    try:
        n = int(n)
    except TypeError:
        raise TypeError("I don't can, without integer")
    
    for number in list:
        if n == number:
            return True
    return False

def list_histogram():
    data = np.random.normal(70,10,100)

    plt.hist(data, bins=15, color='skyblue', edgecolor='black')

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Example Histogram')

    plt.show()

def list_to_string_concatenator():
    list = [1, 2, "abc" ,'d', 3.141, -13]
    newStrin = ""

    for ch in list:
        newStrin += str(ch)

    return newStrin

def even_numbers_until_237():
    numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

    for n in numbers:
        print(n)

        if n == 237:
            return "I'm stop"
        
def unique_colors_finder():
    #Es un conjunto
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    #If use & is "interseccion"
    return color_list_1 - color_list_2

def triangle_area_calculator():
    b = input("Enter the base: ")
    h = input("Enter the height: ")

    try:
        b=float(b)
        h=float(h)
    except ValueError:
        raise ValueError("I don't can, without float number")
    
    return(f"Area: {(b*h)/2}")
#30 ^^^^^^^^^^^^^^^^^^^^^^^^^^
def gcd_number(n):
    lista = []
    for i in range(1,n+1):
        if n % i == 0:
            lista.append(i)
    
    return set(lista)

def gcd_calculator():
    n1 = input("Enter the number: ")
    n2 = input("Enter the number: ")

    try:
        if int(n1)>0 and int(n2)>0:
            n1 = int(n1)
            n2 = int(n2)
        else:
            raise ValueError("I don't can, without int number positive")
    except ValueError:
        raise ValueError("I don't can, without int number positive")
    
    lista1 = gcd_number(n1)
    lista2 = gcd_number(n2)

    return(max(lista1 & lista2))

def lcm_calculator():
    n1 = input("Enter the number: ")
    n2 = input("Enter the number: ")

    try:
        if int(n1)>0 and int(n2)>0:
            n1 = int(n1)
            n2 = int(n2)
        else:
            raise ValueError("I don't can, without int number positive")
    except ValueError:
        raise ValueError("I don't can, without int number positive")
    
    return n1 * n2 /gcd(n1,n2)

def lcm_calculator2(numbers):
    return reduce((lambda x, y: int(x*y/gcd(x,y))),numbers)

def triple_sum_with_equality_rule():
    n1 = input("Enter a integer: ")
    n2 = input("Enter a integer: ")
    n3 = input("Enter a integer: ")

    try:
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
    except ValueError:
        raise ValueError("I don't can, without intenger")
    
    if n1 == n2 or n2 == n3 or n1 == n3:
        return 0
    return n1+n2+n3

def conditional_sum_to_20():
    n1 = input("Enter a integer: ")
    n2 = input("Enter a integer: ")

    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        raise ValueError("I don't can, without intenger")
    
    if n1 + n2 > 15 and n1 + n2 < 20:
        return 20
    return n1 + n2

def equality_or_5_rule_checker():
    n1 = input("Enter a integer: ")
    n2 = input("Enter a integer: ")

    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        raise ValueError("I don't can, without intenger")
    
    if n1 == n2 or abs(n1 - n2) == 5 or n1 + n2 == 5:
        return True
    return False

def add_integers_validator():
    n1 = int(input("Enter a integer: "))
    n2 = int(input("Enter a integer: "))

    if not(isinstance(n1,int) or isinstance(n2,int)):
        raise TypeError("This arguments is not numbers")
    
    return n1 + n2

def personal_info_formatter():
    name = input("Enter your first name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")

    return("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))