import sys

import sr_dummy

sys.modules['sr'] = sr_dummy
import copy
from simulator.vision import *

from test_helper import run_common_tests, failed, passed, import_task_file


class Marker(sr_dummy.Marker):
    def __init__(self, type):
        self.info = MarkerInfo(0, type, 0, 1)


def test_answers():
    task = import_task_file()
    markers = [Marker(MARKER_POISON_TOKEN), Marker(MARKER_TOKEN), Marker(MARKER_TOKEN), Marker(MARKER_TOKEN)]
    filtered_markers = task.find_token_markers(markers)
    if not filtered_markers:
        failed("Your find_tokens_markers must return something")
    elif filtered_markers is [x for x in markers if x.info.marker_type is MARKER_TOKEN]:
        passed()
    else:
        failed("Your function find_token_markers code doesn't return a correct value")

    filtered_markers = task.find_poison_markers(markers)
    if not filtered_markers:
        failed("Your find_poison_markers must return something")
    elif filtered_markers is [x for x in markers if x.info.marker_type is MARKER_POISON_TOKEN]:
        passed()
    else:
        failed("Your function find_poison_markers code doesn't return a correct value")


if __name__ == '__main__':
    run_common_tests()
    test_answers()
