'''
This is a dummy student code file, which attempts to use as much of the
SR API as it can, in as many ways as is sane and some that aren't.
This should not be considered a reference for the API, instead you should
read the docs (http://srobo.org/docs/programming), or see the trac page
about the API: http://srobo.org/trac/wiki/RobotAPI.
'''

import sr
from sr import *

R = sr.Robot()

print R.usbkey
print R.startfifo
print R.mode
print R.zone
print R.power.battery.voltage, R.power.battery.current

MY_OTHER_COND = ( R.io[0].input[1].query.a > 1.6,
            (R.io[0].input[2].query.d == 1) & (R.io[0].input[3].query.d == 0) )

def wait_things():
    '''
    Explore wait_for
    '''

    # set motor 0 to 20% power ahead
    R.motors[0].target = 20

    # wait for a button to be pressed.
    sr.wait_for( R.io[0].input[0].query.d == 1 )

    # stop the motor
    R.motors[0].target = 0

    res = sr.wait_for( R.io[4].input[1].query.d )

    # Wait for digital input pin 3 on JointIO board 0 to change value
    res = sr.wait_for( R.io[0].input[3].query.d )

    # Wait for digital input 3 on JointIO board 0 to become digital '1'
    res = sr.wait_for( R.io[0].input[3].query.d == 1 )

    # Wait for the reading of analogue input 3 on JointIO board 0 to exceed 1V
    res = sr.wait_for( R.io[0].input[1].query.a > 1 )

    # Wait for the reading of analogue input 2
    # on JointIO board 0 to drop below 2.5V
    res = sr.wait_for( R.io[0].input[2].query.a < 2.5 )

    # OR:
    res = sr.wait_for( R.io[0].input[3].query.d == 1,
                        R.io[0].input[2].query.d == 0 )
    res = sr.wait_for( R.io[0].input[3].query.a > 2,
                        R.io[0].input[3].query.a < 3 )

    # AND:
    res = sr.wait_for( (R.io[0].input[3].query.d == 1)
                        & (R.io[0].input[2].query.d == 0) )

    # alternatively:
    res = sr.wait_for( And( R.io[0].input[3].query.d == 1,
                            R.io[0].input[2].query.d == 0 ) )

    print res[0]

    # mix and match
    sr.wait_for( R.io[0].input[1].query.a > 1.6,
                    (R.io[0].input[2].query.d == 1)
                    & (R.io[0].input[3].query.d == 0)
                )

    # this could also happen outside main
    my_cond = ( R.io[0].input[1].query.a > 1.6,
            (R.io[0].input[2].query.d == 1) & (R.io[0].input[3].query.d == 0) )

    sr.wait_for( my_cond )
    # Use the one defined outside main
    sr.wait_for( MY_OTHER_COND )

    # You can even be really clever:
    res = sr.wait_for( my_cond = MY_OTHER_COND )
    if res.my_cond:
        print 'yay'


def vision_things():
    '''
    Explore vision things
    '''

    # see what we can
    markers = R.see( res = (42, 19) )

    # see what we can
    markers = R.see( stats = True )

    # see what we can
    markers = R.see( res = (42, 19), stats = True )

    # see what we can
    markers = R.see()

    print "All marker types: ", MARKER_ARENA, MARKER_ROBOT, MARKER_PEDESTAL, MARKER_TOKEN

    for marker in markers:
        print marker
        print marker.info
        print marker.info.code
        print marker.info.marker_type
        print marker.info.offset
        print marker.info.size
        print marker.timestamp
        print marker.res
        print marker.res[0]
        print marker.res[1]
        print marker.vertices
        print len(marker.vertices)
        print marker.vertices[0]
        print marker.centre
        print marker.centre.image
        print marker.centre.image.x
        print marker.centre.image.y
        print marker.centre.world
        print marker.centre.world.x
        print marker.centre.world.y
        print marker.centre.world.z
        print marker.centre.polar
        print marker.centre.polar.length
        print marker.centre.polar.rot_x
        print marker.centre.polar.rot_y
        print marker.dist
        print marker.rot_y
        print marker.orientation
        print marker.orientation.rot_x
        print marker.orientation.rot_y
        print marker.orientation.rot_z

def io_things():
    '''
    Explore io things
    '''

    # R.io[IO_BOARD_NUMBER].input[PIN_NO].query.d

    # to read JoinIO board 0's digital pin 0...
    pin0 = R.io[0].input[0].d

    # R.io[IO_BOARD_NUMBER].input[PIN_NO].query.a

    # to read JoinIO board 0's analogue pin 2...
    pin0 = R.io[0].input[2].a

    # R.io[IO_BOARD_NUMBER].output[PIN_NO].query.d = VALUE

    # to set JointIO board 0's pin 1 high:
    R.io[0].output[1].d = 1

    # to set JointIO board 0's pin 1 low:
    R.io[0].output[1].d = 0

    R.motors[0].target = 50   # WILL work, if motor 0 exists
    R.motors[1].target = -20  # WILL work, if motor 1 exists
    R.motors.target = 42      # WON'T WORK

    # the above is similar to the situation for 'io' and 'servo'

    print pin0

def power_things():
    '''
    Explore power things
    '''

    # turn LED 0 on
    R.power.led[0] = 1       # WILL work
    R.power.led = 0          # WON'T WORK
    R.power[0].led[0] = 1    # WON'T WORK

    # to toggle LED 2, you can use
    R.power.led[2] = not R.power.led[2]

    R.power.beep(440, 0.5)

    # beep at 100Hz for 1s, then at 200Hz for 2s
    R.power.beep( [(100, 1), (200, 2)] )

    # ramp up from 100Hz to 1000Hz in 1s overall, with frequency jumps of 100Hz
    R.power.beep( [ (x*100, 0.1) for x in range(1, 10) ] )

    # servo[N][SERVO_NUMBER] = POS

    # set servo 1's position (on PWM board 0) to 50.0
    R.servos[0][1] = 50.0

    # variable = pwm[N][SERVO_NUMBER]

    # store the position of PWM board 0's servo 0 in 'bees'
    bees = R.servos[0][0]

    print bees

if __name__ == '__main__':
    io_things()
    power_things()
    vision_things()
    wait_things()
