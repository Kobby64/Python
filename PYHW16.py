# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:19:00 2020

@author: ofori
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:32:52 2020

@author: ofori
"""

"""Work In Progess"""

#numpy package to calculate log
import numpy as np

# add function for addition
def add(x, y):
 return x + y

# subtract function used for subtraction
def subtract(x, y):
 return x - y

# multiply function used for multiplication
def multiply(x, y):
 return x * y

# divide function used for divide the two numbers
def divide(x, y):
 return x / y
# for natural log
def naturalLogarithm(x):
 return np.log(x)
# for base10 log

def base10Logarithm(x):
 return np.log10(x)
# for base2 log

def base2Logarith(x, y):
 return np.log2(x)

# Printing some format
print("what format you expect the expression to be entered in")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Natural logarithm")
print("6.Base10 logarithm")
print("7.Base2 logarithm")

choice = input("Enter your preferred choice(1/2/3/4/5/6/7): ")
# taking user input using num1
num1 = int(input("Enter first Number: "))  
 # taking user input using num2
num2 = int(input("Enter Second Number: "))  


#try block
try:
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        print("Natural log of", num1, "=", naturalLogarithm(num1))
        print("Natural log", num2, "=", naturalLogarithm(num2))

    elif choice == '6':
        print("Base10 log of", num1, "=", base10Logarithm(num1))
        print("Base10 log of", num2, "=", base10Logarithm(num2))

    elif choice == '7':
        print("Base2 log of", num1, "=", base2Logarith(num1))
        print("Base2 log of", num2, "=", base2Logarith(num2))

    else:
        print("There is some invalid input")
        #Exception block executes if any kind of exception program find
except Exception:
    print("There is some exception....\nplease try to fix as soon as possible.")
