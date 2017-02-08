'''Homework for Chapter 2
Name: Bailey Kindrick 
I certify that is entirely my work. 
Chapter 2
Book questions (30%)
T/F
1. F
2. T
3. F
4. T
5. F
6. T
7. T
8. F
9. T
10. F

Multiple Choice
1. C
2. A
3. D
4. A
5. B
6. D
8. A
10. D

Discussion
4a. 0
    1
    4
    9
    16
4b. TypeError: 'type' object is not subscriptable 
4c. Hello
    Hello
    Hello
    Hello
4d. 0 1
    1 2
    2 4
    3 8
    4 16
5. It is a good idea to write in pseudocode because it will allow you to formulate your ideas without worrying about the rules of Python.
6. The 'sep' parameter can be utilized in a print statement on any character, string, or integer. The ‘sep’ parameter is also to format output statements with strings.
7. What prints when the code is executed?

Programming Exercises (70%)
'''
# Example worked for you.
# Write a program that inputs numbers separated by a comma
# and then uses a loop to add the numbers
def addNums():
    # Input the numbers from the user
    numbers = eval(input('Input some numbers separated by a comma: '))

    # Initialize a variable to use to add the numbers
    total = 0

    # Loop through the numbers to add them all to total
    for num in numbers:
        total = total + num

    # Print the result to the shell
    print('The total of the numbers is:',total)

addNums()

# Exercise 2 Change program to get average of 3 scores and change the comments
# names, etc to match the new program.

# avg2.py
#   A simple program to average two exam scores  
#   Illustrates use of multiple input

def avg3():
    print("This program computes the average of three exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

avg3()

# Exercise 4 Modify program to compute and print a table of Celsius
# values and the Fahreneit equivalent every 10 degrees from 0 to 100.

# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def convert():
 
   print("This program prints a table of celsius and fahrenheit temperatures")
   print("every 10 degrees from 0C to 100C")
   celsius = 0 
   fahrenheit = 9/5 * celsius + 32
   for i in range(0, 101, 10):
       newcelsius = i 
       newfahrenheit = 9/5 * newcelsius + 32
       print("celsius", newcelsius, "fahrenheit", newfahrenheit)
           
convert()

# Exercise 5  Modify the program so that years is a user input
# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def futval():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    yr = eval(input("Enter the number of years: "))
    for i in range(yr):
        principal = principal * (1 + apr)

    print("The value in 10 years is:", principal)

futval()

# Last exercise (not in the book) Write a program that inputs
# numbers separated by a comma and then uses a loop to add the
# inverse (1/x) of the numbers, i.e. (1/x + 1/x + ...), and to add
# the square (x ** 2) of each number (x ** 2 + x ** 2 + ...).

def addInverse():
    numbers = eval(input("Input some numbers seperated by a comma: "))
    inverseTot = 0
    squareTot = 0
    for num in numbers:
        inverseTot = inverseTot + 1/num
        squareTot = squareTot + num ** 2
    print("Inverse Total: ", inverseTot, "Square Total: ", squareTot)
addInverse()
