import time

from sr import *

R = Robot()

def turn(speed, duration):
    """
    Turn around at speed with duration
    """
    # Set both motors to turn with a target of 'speed'
    # One of them should be negative
    R.motors[0].target = speed
    R.motors[1].target = -speed

    # Wait for 'duration' seconds for the robot to turn
    time.sleep(duration)

    # Stop the motors
    R.motors[0].target = 0
    R.motors[1].target = 0

def find_token_markers(see_output):
    """
        This should return a list of of markers which represent a token
        (of type MARKER_TOKEN)
    """
    token_markers = []
    marker_type_i_want = MARKER_TOKEN
   # Add your code here!

def find_poison_markers(see_output):
    """
        This should return a list of of markers for the poison token
    """
    token_markers = []
    marker_type_i_want = MARKER_POISON_TOKEN
    # Add your code here!

# Turn to the right to see the markers next to the robot
turn(100, 0.31)

print "looking..."

# Get what the robot can see
see_output = R.see()

# Find the markers
token_markers = find_token_markers(see_output)

# Print the results
for marker in token_markers:
    print "Marker seen,", marker.dist, "metres Away!"
