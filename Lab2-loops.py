"""
Lab2-loops.py for the 4 problems assigned in Lab 2

Name:  
"""
def main():
    coffee()
    newton(2,1000)
    newton(5,1000)
    calc_pi(10)
    calc_pi(100000)
    piAlt(10)
    piAlt(1000)
    piAlt(100000)

def order(pounds):
    """
    Write a function, order(pounds), to compute the cost of a coffee order
    for customers. The coffee costs $10.50 per pound. Shipping costs 
    $0.86 per pound, and there is a fixed cost of $1.50 per order for overhead.
    For each order display the cost, "This order costs $"..... Call the order 
    program from the coffee() program.
    """

    # Calculate cost of the order
    cost = (pounds * 10.50) + (pounds * 0.86) + 1.50

    # Print out the cost of the order
    print("The cost of the order is: ", cost)

def coffee():
    """
    Write a function, coffee(), to compute the cost of coffee orders for
    customers. First ask how many coffee orders are to be processed.
    For each order, ask the user for the number of pounds in that order
    then call the order(pounds) program to calculate and display the cost.
    Demonstrate for the instructor.
    """
    # Ask the user how many coffee orders are to be processed
    n = eval(input("How many coffee orders are to be processed: "))
    
    # Loop to place that many orders
    for i in range(n):
          
        # Ask the user how many pounds in this order?
        pounds = eval(input("How many pounds in this order: "))

        # Call the order(pounds) function with the number of pounds
        order(pounds)       

def newton(x, n):
    """
    Write a function, newton(x,n), that approximates the square root of
    the number, x, using Sir Isaac Newton's method.  x / 2 is a good first
    approximation. Repeat the estimate for n times.
    """
    # Initialize approx to x / 2
    
    
    # Loop n times to calculate the new approximation


        # Equation to calculate the new approx from the old



    # Display the number of times, (n), and the resulting approximation of the square
    # root



def calc_pi(n):
    """
    Write a function calc_pi(n) that approximates the value of pi using the
    Wallis formula on your sheet. The program should compute the product
    of the n terms, and output the resulting approximation of pi.
    """

    # Set the initial conditions for your loop


    # Loop n times to compute the product of n terms


        # Write the product accumulator statement


        # Compute the next numerator and denominator


    # Output the resulting approximation of pi (NOT pi / 2)
    

def piAlt(n):
    """
    Write a function piAlt() that approximates the value of Pi using the
    Leibniz series. Print the number of terms and the value of pi for
    the series.
    """
    # Set the initial conditions for your loop


    # Loop n times to compute the sum of n terms


        # Write the accumulator statement


        # Compute the required values for the next term


    # Output the resulting approximation of pi (NOT pi / 4)
    
    
main()



    
    

    

    

