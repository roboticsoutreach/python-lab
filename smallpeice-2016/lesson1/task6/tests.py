import sys
import types

import sr_dummy

sys.modules['sr'] = sr_dummy
import copy
from simulator.vision import *

from test_helper import run_common_tests, failed, passed, import_task_file

MAGIC_NUMBER = 42


class Marker(sr_dummy.Marker):
    def __init__(self, length, rot_y):
        sr_dummy.Marker.__init__(self)
        self.centre = sr_dummy.Point(sr_dummy.ImageCoord(0, 0),
                                     sr_dummy.WorldCoord(0, 0, 0),
                                     sr_dummy.PolarCoord(length, MAGIC_NUMBER, rot_y))
        # aliases
        self.dist = self.centre.polar.length
        self.rot_y = self.centre.polar.rot_y


def test_answers():
    task = import_task_file()
    locations = [(1, 0.5), (2, 30), (9.5, 50), (1.5, -40)]
    markers = [Marker(x, y) for x, y in locations]
    out_locations = task.get_distances(markers)

    if not out_locations:
        failed("Your function must return something")
    elif type(out_locations) is not list or any([(type(x) not in [list, tuple]) or len(x) < 2 for x in out_locations]):
        failed("You should return an array of tuples of two values!")
    out_locations = [(x[0], x[1]) for x in out_locations]
    if set([(x, y) for y, x in out_locations]) == set(locations):
        failed("It seems that you are returning (rot_y, length), instead of (length,rot_y)!")
    elif MAGIC_NUMBER in ([x for _, x in out_locations] + [y for y, _ in out_locations]):
        failed("It seems that you are using rot_x instead of rot_y!")
    elif set(out_locations) == set(locations):
        passed()
    else:
        failed("Your function doesn't return the correct list of outputs")


if __name__ == '__main__':
    run_common_tests()
    test_answers()
