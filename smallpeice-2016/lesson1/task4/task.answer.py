import time

from sr import *

R = Robot()


def turn(R, speed, duration):
    # Set both motors to turn with a target of 'speed'
    # One of them should be negative
    R.motors[0].target = speed
    R.motors[1].target = -speed

    # Wait for 'duration' seconds for the robot to turn
    time.sleep(duration)

    # Stop the motors
    R.motors[0].target = 0
    R.motors[1].target = 0


# make the turn!
turn(R, 100, 0.5)
