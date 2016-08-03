import time

from sr import *

SEARCHING, DRIVING = range(2)

R = Robot()

print "I'm in zone", R.zone


def drive(R, speed, duration):
    R.motors[0].target = speed
    R.motors[1].target = speed
    time.sleep(duration)
    R.motors[0].target = 0
    R.motors[1].target = 0


def turn(R, speed, duration):
    R.motors[0].target = speed
    R.motors[1].target = -speed
    time.sleep(duration)
    R.motors[0].target = 0
    R.motors[1].target = 0

# THESE FUNCTIONS ARE COMMENTED OUT BECAUSE THEY ARE BUILT INTO THE SIMULATOR, BUT NOT INTO THE ROBOTS
# THEY WOULDN'T WORK FOR THE SIMULATOR IF YOU UNCOMMENTED THEM, BUT THEY MIGHT WORK FOR YOUR ROBOT
# (if you use servo 0 and make a grabber)
#
# def grab(R):
#     # Set the servo board 0, port 0's position to 100
#     R.servos[0][0] = 100
#
# def release(R):
#     # Set the servo board 0, port 0's position to 0
#     R.servos[0][0] = 0


# Keep track of the state of the robot
state = SEARCHING


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

# Turn to hopefully see the markers next to us
turn(R, 25, 0.6)

while True:
    if state == SEARCHING:
        print "Searching..."
        # Sleep to reduce motion blur (the robot might still be moving from its momentum)
        time.sleep(0.5)
        tokens = find_token_markers(R.see())
        if len(tokens) > 0:
            m = tokens[0]
            print "Token sighted. {0} is {1}m away, bearing {2} degrees." \
                .format(m.info.offset, m.dist, m.rot_y)
            state = DRIVING

        else:
            print "I Can't see anything."
            turn(R, 25, 0.3)

    elif state == DRIVING:
        print "Aligning..."
        # Sleep to reduce motion blur (the robot might still be moving from its momentum)
        time.sleep(0.5)
        tokens = find_token_markers(R.see())

        if len(tokens) == 0:
            state = SEARCHING

        else:
            # Get the closest token
            tokens.sort(key=lambda x: x.dist)
            m = tokens[0]
            if m.dist < 0.4:
                print "Found it!"
                if R.grab():
                    print "Gotcha!"
                    turn(R, 50, 0.5)
                    drive(R, 50, 1)
                    R.release()
                    drive(R, -50, 0.5)
                else:
                    print "Aww, I'm not close enough."
                exit()  # you might want to remove this if you want to get more than 1 token!

            elif -15 <= m.rot_y <= 15:
                print "Ah, that'll do."
                drive(R, 50, 0.5)

            elif m.rot_y < -15:
                print "Left a bit..."
                turn(R, -12.5, 0.5)

            elif m.rot_y > 15:
                print "Right a bit..."
                turn(R, 12.5, 0.5)
