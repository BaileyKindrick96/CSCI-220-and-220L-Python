"""
Lab3.py

Name:  Bailey Kindrick
        Matt Hancock
"""
from graphics import *
from math import *
def main():
    squares(5)
    rectangle()
    circle()
    cupConverter()
    target()
    triangle()
    movingDot()
   
def squares(numClicks):
    """
    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center
    of the square is at the point where the user clicks. Make the window
    400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the user
    clicks numClics times, and wait for a final click before closing
    the window.
    """
    #Creates a graphical window
    win = GraphWin("Lab 4", 400, 400)
    width = win.getWidth()
    height = win.getHeight()

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to add additional square")
    instructions.draw(win)

    #builds a circle
    shape = Rectangle(Point(20, 20),Point(40,40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click numClicks times to move the
    #circle
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of circle

        #move amount is distance from center of circle to the
        #point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape=shape.clone()
        shape.draw(win)
        shape.move(dx, dy)
        
    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

def rectangle():
    """
    Display the numerical output in the graphics window – don't use print.
    First display instructions to "click twice for the opposite corners of a
    rectangle". Ask the user to "click to end the program", and be sure to
    close the window at the end. Make the window 400 by 400.

    From programming Exercise 9 (p. 119)
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the points and the rectangle. Show the perimeter and
    area of the rectangle on the canvas.

    area = (length)(width)
    perimeter = 2 (length + width)
    """
    
    win = GraphWin("Lab 4", 400, 400)
    width = win.getWidth()
    height = win.getHeight()
    instPt = Point(width/2, height-20)
    instructions = Text(instPt,"Click two corners of a rectangle. \n click again to end the program")
    instructions.draw(win)

    p = win.getMouse()
    x1=(p.getX())
    y1=(p.getY())
    p1=Point(x1,y1)
    p1.draw(win)
    p0 = win.getMouse()
    x2=(p0.getX())
    y2=(p0.getY())
    p2=Point(x2,y2)
    p2.draw(win)
    rect= Rectangle(p1,p2)
    rect.draw(win)
    
    he= abs(x1-x2) 
    le= abs(y1-y2)
    area=le * he
    perim= (2*he) + (2*le)
    area=str(area)
    perim=str(perim)
    tex1= Text(Point(200,200),"the area of the rectangle is: " +(area)+"\n the perimeter is: "+perim)
    tex1.draw(win)

    win.getMouse()
    win.close()
    
    
def findDistance(pt1,pt2):
    # finish writing this function to find the distance and use
    # the function in your circle triangle functions. The inputs, pt1 and
    # pt2 are point objects. Use getX and getY to get the coordinates and
    # use the Euclidean distance formula to calculate the distance.

    x1=pt1.getX()
    x2=pt2.getX()
    y1=pt1.getY()
    y2=pt2.getY()
    distance=(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)
    return distance

def circle():
    """
    Write a function called circle() to draw a circle. The first mouse
    click determines the center of the circle. The second mouse click
    determines a point on its circumference. Use the findDistance(pt1,pt2)
    function to determine the length of the radius. Ask the user to click
    to end the program, and close the window at the end.
    """
    win = GraphWin("Lab 4", 400, 400)
    width = win.getWidth()
    height = win.getHeight()
    instPt = Point(width/2, height-20)
    instructions = Text(instPt,"Click once for the centerpoint. \n click again for a point on the circumference.")
    instructions.draw(win)
    
    pt1 = win.getMouse()
    pt1.draw(win)
    pt2 = win.getMouse()
    pt2.draw(win)
    
    d = findDistance(pt1,pt2)
    print(d)
    circ= Circle(pt1, d)
    circ.draw(win)

    tex1= Text(Point(200,200),"click again to end program")
    tex1.draw(win)

    win.getMouse()
    win.close()

def cupConverter():
    # Author: RoxAnn H. Stalvey, modified by Walter Pharr
    # Illustrates getting numeric input through graphics window

    win = GraphWin("Convert cups to milliliters", 300, 200)

    #Specify the message for the input box
    boxDesc = Text(Point(100, 20), "cups to milliliters: ")
    boxDesc.draw(win)

    #Create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setFill('white')
    inp.setText("0")
    inp.draw(win)
    #Create a Text object for outputting the result
    output = Text(Point(150, 150), "output")
    output.draw(win)

    #This button isn't necessary, but it makes a nice point for the user
    #  to click.  If you click anywhere in the window, the code reacts
    #  the same way.
    button = Text(Point(150, 100), "Click")
    button.draw(win)
    border = Rectangle(Point(115, 80), Point(185, 120))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    cups = eval(inp.getText())

    #Calculate milliliter equivalent here
    cups = cups * 8
    cups = cups  * 29.57
    
    # Display output and change button
    output.setText("milliliters = " + str(cups))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()

def target():
    win = GraphWin("Archery Target", 500, 500)

    # Add code here to get the dimensions and draw the target
    boxDesc = Text(Point(100, 20), "enter radius (10-28) ")
    boxDesc.draw(win)

    inp = Entry(Point(200, 50), 5)
    inp.setFill('white')
    inp.setText("0")
    inp.draw(win)
    win.getMouse()
    
    rad = eval(inp.getText())

    circ1= Circle(Point(250,250), (rad * 9))
    circ1.setOutline("white")
    circ1.setFill("white")
    circ1.draw(win)               

    circ2= Circle(Point(250,250), (rad * 7))
    circ2.setOutline("black")
    circ2.setFill("black")
    circ2.draw(win)

    circ3= Circle(Point(250,250), (rad * 5))
    circ3.setOutline("blue")
    circ3.setFill("blue")
    circ3.draw(win)

    circ4= Circle(Point(250,250), (rad * 3))
    circ4.setOutline("red")
    circ4.setFill("red")
    circ4.draw(win)

    circ5= Circle(Point(250,250), rad)
    circ5.setOutline("yellow")
    circ5.setFill("yellow")
    circ5.draw(win) 


    # Wait for another click to exit
    win.getMouse()
    win.close()

def triangle():
    '''This function draws an archery target consisting of a central
    circle of yellow surrounded by concentric rings of red, blue,
    black and white. Each ring has the same width showing which is the
    same as the radius of the yellow circle. Use the findDistance function
    to determine the length of each side. READ THE INSTRUCTIONS.'''
    
    win = GraphWin("Draw a Triangle", 500, 500)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    width = win.getWidth()
    height = win.getHeight()
    instPt = Point(width/2, height-20)
    instructions = Text(instPt,"Click three times to make a triangle. \n click again to end the program")
    instructions.draw(win)

    pt1= win.getMouse()
    pt1.draw(win)
    pt2 = win.getMouse()
    pt2.draw(win)
    pt3 = win.getMouse()
    pt3.draw(win)
    tri= Polygon(pt1,pt2,pt3)
    tri.draw(win)
    

    t1=findDistance(pt1,pt2)
    t2=findDistance(pt1,pt3)
    t3= findDistance(pt3,pt2)
    print(t1,t2,t3)
    s = (t1+t2+t3)/2
    area = (s*(s-t1) * (s-t2) * (s-t3)) ** (1/2)
    area=str(area)
    tex1= Text(Point(200,200),"the area of the triangle is: " +(area))
    tex1.draw(win)


    # Wait for another click to exit
    win.getMouse()
    win.close()

def movingDot():
    """
    Display a dot (radius is 50 pixels) in the top left portion of
    the canvas with a message, “click to begin moving the dot”. After
    a click, the message changes to “dot moves 20 times” and the dot
    moves from the top left to the top right, then to the bottom right
    and then to the bottom left and returns to the top left. The dot
    makes 5 complete rotations around the canvas and stops. Then
    the message changes to “click to close” and another click
    closes the window. See the window below. Use a sleep(0.2)
    before every move so the user can see the dot move.
    """
    win = GraphWin("Moving Dot", 300, 300)
    # Add code here to accept the mouse clicks, move the dot
    # and close the graphics window.

    sleep(0.2)
    

main()



    
    

    

    

