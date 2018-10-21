#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
import random

def assignment_1(kame, use_for=True):
    """ Assignment 1: 
    
    Draw a square with a side length of 150
    
    Args:
          kame (object): an object of Turtle
    
    Kwargs:
        use_for (bool) : it will use for loop by default.
                         otherwise use while loop.
    Returns:
        None
    """
    kame.clear() # clear the screen
    if use_for:
        # use for loop
        for i in range(0, 4):
            kame.forward(150)
            kame.left(90)
    else:
        # use while loop
        i=0
        while i<4:
          kame.forward(150) 
          kame.left(90)
          i += 1


def assignment_2(kame):
    """ Assignment 2: 
        Draw an equilateral triangle
    
    Args:
        kame (object): an object of Turtle

    Kwargs:

        None

    Returns:
        None
    """
    kame.clear() # clear the screen
    for i in range(0, 3):
        kame.forward(150)
        kame.left(120)



def extra_assignment_1(kame, length=100):
    """ Extra assignment 1: 
        Draw a star
    
    Args:
        kame (object): an object of Turtle

    Kwargs:

        length (int): specify the length of a star, default is 100.

    Returns:
        None
    """
    kame.clear()
    angle = 180 - 36 
    for i in range(5):
        kame.forward(length)
        kame.right(angle)
        

def extra_assignment_2(kame, radius=100, maxiter=1000):
    """ Extra assignment 2: 
    
        The turtle will randomly move within a circle of given radius.
        
    Args:
        kame (object): an object of Turtle

    Kwargs:

        radius (int): the radius of a circle where the turtle randomly moves.
                      default is 100.
        maxiter(int): the maximum iteration. default is 1000.
    
    Returns:
        None
    """
    kame.clear()
    # make the circle to the origin at (0, 0)
    kame.penup()
    kame.goto(0, -radius)
    kame.pendown()
    kame.circle(radius) # draw a circle of the radius
    kame.speed(0) # fastest speed
    iter_counter = 0
    while iter_counter < maxiter:
        direction = random.randint(0, 3) # Find a random number from 0 to 3
        angle = direction * 90 # Convert to 0, 90, 180, or 270
        kame.left(angle)       # Change the direction by the angle obtained above
        kame.forward(10)       # Go forward 10
        d = kame.distance((0.0, 0.0))
        if d > radius:
            kame.undo()
        elif d == 0:
            # back to the origin
            break
        iter_counter += 1
    
        

def koch(kame, length, level):
    """ Extra assignment 3: 
        
        Draw a fractal graph by koch curve
    
    Args:
        kame (object): an object of Turtle
        length (int) : the length of koch curve
        level  (int) : the level of the koch curve. 
                       It should be greater than or equal to 0.

    Kwargs:

        None

    Returns:
        None
    """
    kame.speed(0)
    if level < 0:
        print("ValueError: the parameter level should be "
              "greater than or equal to 0.") 
        return
    elif level == 0:
        kame.forward(length)
        return
    else:
        #for angle in [60, -120, 60, 0]:
        #    koch(kame, length/3, level-1)
        #    kame.left(angle)
        new_length = length / 3
        koch(kame, new_length, level-1)
        kame.left(60)
        koch(kame, new_length, level-1)
        kame.right(120)
        koch(kame, new_length, level-1)
        kame.left(60)
        koch(kame, new_length, level-1)
    

def extra_assignment_4(kame):
    """ Extra assignment 4: 
        Draw a koch snowflake.
    
    Args:
        kame (object): an object of Turtle

    Kwargs:

        None

    Returns:
        None
    """
    kame.clear() 
    # move to the the point at (-150, 0)
    kame.penup()
    kame.home()
    kame.backward(150)
    kame.pendown()
    kame.speed(0)
    for i in range(3):
        # draw koch curve with the length of 200 and the level of 3 
        koch(kame, 200, 3)
        kame.right(120)


if __name__ == '__main__':
    
    # preparation 
    win = turtle.Screen()
    
    kame = turtle.Turtle() # create an object of kame
    kame.shape('turtle')   # change the shape of kame
    kame.backward(100)     # move to (-100, 0) as start point
    
    assignment_1(kame)
    # press any key
    key = input('Press Enter to continue')
    
    assignment_2(kame)
    key = input('Press Enter to continue')
    
    extra_assignment_1(kame)
    key = input('Press Enter to continue')
    
    #turtle.speed("fastest")
    extra_assignment_2(kame)
    key = input('Press Enter to continue')
    #kame.clear()
    
    # back to home
    kame.clear()
    koch(kame, 300, 4)
    key = input('Press Enter to continue')
    
    #
    extra_assignment_4(kame)
    
    # wait for a user click on the canvas
    win.exitonclick()    
    # Control the main window
    win.mainloop()
