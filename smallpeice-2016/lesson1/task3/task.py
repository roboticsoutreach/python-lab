# import the 'time' module, which (among other things) lets you wait for a given time.
import time

from sr import *
R = Robot()


def turn_right():
    # Set the 0'th motor (the left one) to full power (100):
    R.motors  # Add your code here

    # Wait for a quarter of a second for the robot to turn
    time.sleep(0.25)

    # Set the 0'th motor (the left one) to off (0):
    R.motors  # Add  your code here!

# make the turn!
turn_right()
