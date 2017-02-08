"""
Lab1.py for the 5 problems assigned in Lab 1

Name:  <Bailey Kindrick>
"""
def main():
    kilometersToMiles()
    shootingPercentage()
    coffee()
    triangleArea()
    sphere()

def kilometersToMiles():
    """
    Compute the number of miles that John will travel, given the
    kilometers. Input the kilometers, compute the miles (1 mile =
    1.61 kilometers), and display the number of miles.     
    """
    miles = 1.61
    # Get from user how many kilometers?
    kilometers = eval(input("How many kilometers is John driving?"))

    # Calculate the number of miles
    totalMiles = kilometers / miles

    # Display the miles
    print("The number of miles John drove is: ", totalMiles)


def shootingPercentage():
    """
    Compute the shooting percentage, given the number of shots taken
    and the number of shots made.
    """
    # Get from user how many shots were taken?
    totalShots = eval(input("Enter total number of shots"))

    # Get from user how many shots were made?
    shotsMade = eval(input("Enter total number of shots made"))

    # Calculate the shooting percentage
    shotPercentage = (shotsMade / totalShots) * 100

    # Display the percentage
    print("The percentage of total shots is: ", shotPercentage)

def coffee():
    """
    Compute the cost of a coffee order. Each order costs $10.50 per pound.
    Each order ships for $0.86 per pound, and there is a fixed cost of
    $1.50 per order for overhead.
    Ask the user for the number of pounds in the order. Then calculate
    and display the cost. 
    """
    # Get from user how many pounds in this order?
    pounds = eval(input("Enter total amount of pounds in this order"))

    # Calculate cost of the order
    cost = (pounds * 10.50) + (pounds * 0.86) + 1.50
    # Display the cost of the order
    print("cost", cost)


def triangleArea():
    """
    Calculate the area of a triangle given the length of its three sides,
    a, b, and c, using the formulas in the document. The square root can
    be expressed as raised to the 0.5 power. See Lab1.doc for the formula.
    """

    # Input from user the lengths of the 3 sides
    sides = eval(input("Enter the length of the 3 sides"))

    # Calculate s
    a = eval(input("Enter length of side a"))
    b = eval(input("Enter length of side b"))
    c = eval(input("Enter length of side c"))
    s = ((a + b + c)/2)
    # Calculate A
    totalArea = (s * (s - a) *(s - b) * (s - c))**0.5
    # Display the area
    print("The area is:", totalArea)


def sphere():
    """
    Calculate the volume and surface area of a sphere given its radius,
    using the formulas in the document.
    """
    pi = 3.14159

    # Input from the user the radius
    r = eval(input("Enter the radius of the given sphere"))
    
    # Calculate the volume and surface area
    V = ((4 / 3) * pi * (r**3))
    A = (4 * pi * (r**2))

    # Display the volume and surface area
    print("The volume and surface is:", V, A) 

main()





    
    

    

    

