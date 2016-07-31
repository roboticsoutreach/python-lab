import time

from sr import *

R = Robot()


def turn(R, speed, duration):
    # Set both motors to turn with a target of 'speed'
    # One of them should be negative
    R.motors[0] # Add here
    R.motors[1] # Add here

    # Wait for 'duration' seconds for the robot to turn
    time.sleep(duration)

    # Stop the motors
    R.motors[0] # Add here
    R.motors[1] # Add here


# make the turn!
turn(R, 100, 0.5)
