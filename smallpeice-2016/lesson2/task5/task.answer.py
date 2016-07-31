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
    for marker in see_output:
        if marker.info.marker_type == marker_type_i_want:
            token_markers.append(marker)
    return token_markers

# Turn to the right to see the markers next to the robot
turn(100, 0.15)

print "looking..."

# Get what the robot can see
see_output = R.see()

# Find the markers
token_markers = find_token_markers(see_output)

# Print the results
for marker in token_markers:
    print "Marker seen,", marker.dist, "metres Away!"
