'''
This is a dummy implementation of the SR API, as documented at:
* http://trac.srobo.org/wiki/RobotAPI
* http://srobo.org/docs/programming/
This should not be considered canonical!
'''

# Imports
from collections import namedtuple as __namedtuple__

# Constants
MARKER_ARENA = MARKER_ROBOT = MARKER_TOKEN = MARKER_PEDESTAL = 13

robot = None

# Power

class Battery:
    def __init__(self):
        self.voltage = 12.3
        self.current = 1.3

class Power:
    def __init__(self):
        self.led = [0,1,2,3,4,5,6,7]
        self.battery = Battery()

    def beep(self, hz, time=1):
        pass

class Motor:
    def __init__(self):
        self.target = 0

class Input:
    def __init__(self):
        self.d = 0
        self.a = 0.0

class Output:
    def __init__(self):
        self.d = 0

class JointIO:
    def __init__(self):
        self.input = [Input() for x in range(8)]
        self.output = [Output() for x in range(8)]

# Vision

MarkerInfo = __namedtuple__( "MarkerInfo", "code marker_type offset size" )
ImageCoord = __namedtuple__( "ImageCoord", "x y" )
WorldCoord = __namedtuple__( "WorldCoord", "x y z" )
PolarCoord = __namedtuple__( "PolarCoord", "length rot_x rot_y" )
Orientation = __namedtuple__( "Orientation", "rot_x rot_y rot_z" )
Point = __namedtuple__( "Point", "image world polar" )

class Marker:
    def __init__(self):
        # Aliases
        self.info = MarkerInfo(0, 13, 0, 1)
        self.timestamp = 3.14159
        self.res = (800, 600)
        self.vertices = []
        self.centre = Point(ImageCoord(0, 0), WorldCoord(0, 0, 0), PolarCoord(1, 0, 0))
        self.dist = 42
        self.rot_y = 13
        self.orientation = Orientation(0, 0, 0)

# Logic Expressions

def And(*args):
    return args

def Or(*args):
    return args

# Robot

class Robot:
    def __init__(self):
        self.usbkey = None
        self.startfifo = None
        self.mode = None
        self.zone = None
        self.motors = [Motor(), Motor()]
        self.io = [JointIO()]
        self.power = Power()
        self.servos = [[0] * 8]
        global robot
        robot = self

    def see(self, res = (800, 600), stats = False):
        """
        Make the robot see stuff
        """
        return [Marker()]

def wait_for( *polls, **named ):
    """
    Wait for at least one of the passed polls to happen
    """
    C = __namedtuple__( "WaitResults", named.keys )
    return C( **named )
