'''
Name: Bailey Kindrick 

Chapter 4 T/F 1-10
1. F
2. T
3. T
4. F
5. T
6. F
7. T
8. F
9. F
10. F

Chapter 4 Multiple Choice 1-9
1. D
2. B
3. D
4. C
5. D
6. D
7. D
8. B
9. A

Purpose: A simple program that allows individuals to play tic-tac-toe. 

Inputs:
1. The first player clicks to place a x 
2. The second player clicks to place an o
3. Click to close the window 

Outputs:
1. x is shown in window
2. o is shown in window 
3. the window closes and the game ends

Step by step in English (Psuedocode). Include these as comments in the program.

Authenticity:
  I certify that this program is entirely my work.


'''
from graphics import *

def main():
    # Create the canvas and the tic-tac-toe grid 
    win = GraphWin('Tic-Tac-Toe',300,300)
    p1 = Point(100,0)
    p2 = Point(100,300)
    line1 = Line(p1,p2)
    line1.draw(win)
    p3 = Point(200,0)
    p4 = Point(200,300)
    line2 = Line(p3,p4)
    line2.draw(win)
    p5 = Point(0,100)
    p6 = Point(300,100)
    line3 = Line(p5,p6)
    line3.draw(win)
    p8 = Point(0,200)
    p9 = Point(300,200)
    line4 = Line(p8,p9)
    line4.draw(win)

    # Loop 4 times to draw 4 X's and 4 O's
    for i in range(4):

        # get the mouse click for the X
        pt1 = win.getMouse()
        
        # call centerPt(pt) to center the point
        pt1 = centerPt(pt1)
        
        # call the drawX(pt,win) to draw the X
        drawX(pt1,win)
        
        # get the mouse click for the O
        pt1 = win.getMouse()
        
        # call centerPt(pt) to center the point
        pt1 = centerPt(pt1)
        
        # call the drawO(pt,win) to draw the O
        drawO(pt1,win)

    # get the mouse click for the last X
    pt1 = win.getMouse()
    
    # call centerPt(pt) to center the point
    pt1 = centerPt(pt1)
    
    # call the drawX(pt,win) to draw the X
    drawX(pt1,win)
    
    # draw instructions to click again to close
    Text(Point(150,150),"Click again to close").draw(win)
    win.getMouse()
    win.close()
    
    # wait for mouse click and close the window


# Write the function to center the point
def centerPt(pt):
    '''pt is a point object, return a centered point object'''
    pt = Point(pt.getX(),pt.getY())
    
    #get the x and y coordinates
    x = pt.getX()
    y = pt.getY()  

    # calculate the x and y that is in the center of the square
    xNew = x // 100 * 100 + 50
    yNew = y // 100 * 100 + 50

    # return the centered point object
    return Point(xNew, yNew)

# Write the function to draw the X
def drawX(pt, win):
    ''' pt is a point object at the center of the X and win is the
    graphics window where the X will be drawn.'''
    textX = Text(pt, "X")
    textX.draw(win)
    textX.setSize(36)
    
# Write the function to draw the O
def drawO(pt, win):
    ''' pt is a point object at the center of the O and win is the
    graphics window where the O will be drawn.'''
    textO = Text(pt, "O")
    textO.draw(win)
    textO.setSize(36)

main()
    
    
