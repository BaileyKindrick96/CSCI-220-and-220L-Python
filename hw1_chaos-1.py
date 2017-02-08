'''
Answer the following questions from the end of chapter 1.
Multiple choice
2. D
5. B
8. B
9. A
10. D

Discussion
1c. Describe the difference between a programming language and natural language
A natural languauge is a language spoken by people to communicate to other people. A programming language is a language utilized by a person to convert a natural language into a language that a machine can communicate with. 
1e. Describe the difference between an interpreter and a compiler
An interpreter: writes a program, then runs/debugs or writes a line of code and then executes it. A compiler: writes a program, compiles, then runs/debugs. 
1f. Describe the difference between syntax and semantics
Syntax is precise form, while semantic is precise meaning.
Programming exercise Type exactly what will print. (Example shown for 1a.)
1a. print("Hello, world!") ---> Hello, world!
1b. print("Hello") ---> Hello
1c. print(3) ---> 3
1d. print(3.0) ---> 3.0
1e. print(2 + 3) ---> 5
1f. print(2.0 + 3.0) ---> 5.0
1g. print("2" + "3") ---> 23
1h. print("2 + 3 =", 2 + 3) ---> 2 + 3 = 5
1i. print(2 * 3) ---> 6
1j. print(2 ** 3) ---> 8
1k. print(2 / 3) ---> 0.6666666666666666

'''

# Exercise 4. Modify the chaos program below to print 20 lines instead of 10
def chaos():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)

chaos()

# Exercise 5. Modify the chaos1 program to allow the user to input the number
# of lines to print to get another value from the user using the line:
# n = eval(input("How many numbers should I print?"))
def chaos1():
    def chaos1():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
        
chaos1()

# Exercise 7. Modify the chaos2 program to two inputs from the user and print
# a table with the two columns like in Section 1.8. Don't worry about aligning
# the columns.
def chaos2():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a first number between 0 and 1: "))
    y = eval(input("Enter a second number between 0 and 1: "))
    print("input   0.25          0.26")
    print("--------------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x,y)

chaos2()

# Write a short program to calculate the amount of carpet required.
# Inputs are height and width in inches. The program adds a two inch
# border around the rectangle. The program prints the amount of carpet
# required in square feet. Example: height of 8 inches and width of 4 inches.
# Answer is: (8 + 2 + 2) * (4 + 2 + 2) = 12 * 8 = 96 square inches = .666667 sq ft

def calcCarpet(height,width):
    carpet = ((height + 2 + 2) * (width + 2 + 2)/144)
    print('Carpet required is', carpet, 'Sq. ft.')

calcCarpet(8,4)



