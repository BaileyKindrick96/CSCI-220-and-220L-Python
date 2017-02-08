'''Homework for Chapter 3
Name: Bailey Kindrick 
I certify that is entirely my work
Chapter 3
Book questions (30%)

Multiple Choice
1. C
2. D
3. D
4. B
5. B
6. C
7. D
8. D
9. A

Discussion
1. Show data type by how it is written
    int - no decimal
    float - with decimal
    str - quotes before and after
1a. 7.4 (float)
1b. 5.0 (float)
1c. 18.96296296296297 (float)
1d. (NameError: name 'sqrt' is not defined)
1e. 11.0 (float)
1f. 8 (int)
2a. (3 + 4) * (5) 
2b. (n * (n - 1)) / 2
2e. (y2 -y1) / (x2 - x1) 
3. show list of numbers for each with []'s
3a. [0, 1, 2, 3, 4]
3b. [3, 4, 5, 6, 7, 8, 9]
3c. [4, 7, 10]
3d. [15, 13, 11, 9, 7]
3e. Prints nothing 
4a. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
4b. [1, 27, 125, 343, 729]
4c. [012, 212, 412, 612, 812, done]
4d. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
6a. -4
6b. 2
6c. -4
6d. -2
6e. 3

programs - 70%
'''
def example(n):
    '''create and print a sequence of n numbers beginning with 2 and adding
    2 to each 2nd, 4th, 6th, ... number in the sequence, i.e. 2,4,4,6,6,8,8,...
    '''
    num = 2
    for i in range(n):
        print(num, end = ' ')
        num = num + 2 * ((i+1)%2)
example(7)

def main():
    factorial(4)
    sum_sequence(1,5)
    generate(3,7)
    
def factorial():
    '''Assumes that n is a positive number. Multiplies 1 times 2
    times 3 until n is reached. For n of 3, the result would be
    1 * 2 * 3.
    '''
    # initialize result to 1
    n = eval(input("Please enter number: "))
    result = 1

    # loop n times to get the product
    for i in range(1, n + 1):
       result *= i    
   
    # output the factorial of n is answer
       print("The result is: ", result)
     
factorial()

def sum_sequence():
    '''
    Add the numbers beginning with num1 and continuing through num2.
    '''
    # initialize total for the sum accumulator
    num1 = eval(input("Please enter your first number: "))
    num2 = eval(input("Please enter your second number: "))
    total = 0

    # loop to add all the numbers up to num2
    for i in range(num1, num2 + 1):
        total = total + i

    # print The sum of the numbers from num1 to num2 is total
    print("The sum of the sequence is: ", total)

sum_sequence()
    
def generate():
    '''
    prints n numbers beginning with start, an integer. The sequence
    prints start twice, then adds two and prints that number twice.
    This repeats until n numbers have been printed. For example,
    generate(3,7) would print the following numbers, 3, 3, 5, 5, 7, 7, 9.
    Another example, generate(2,4) would print, 2, 2, 4, 4.
    '''
    # initial value of output to start
    start = eval(input("Enter start value: "))
    n = eval(input("Enter how many outputs you want: "))
      
    # loop n times with (end = ' ') to print n numbers in the loop

    for i  in range(n):
        print(start, end = ' ')
        start = start + 2  * ((i + 2) % 2)
        
    # print nothing to get a new line

generate()
        
main() 
