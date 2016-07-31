import time
import threading
from Queue import Queue
from multiprocessing.pool import ThreadPool
from simulator.vision import *


from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


class Motor(object):
    def __init__(self):
        self.target = 0

class Marker(object):
    def __init__(self, type):
        this.info.


class RSim(object):
    def __init__(self):
        self.motors = [Motor(), Motor()]

    def see(self):
        return [] #TODO


def test_answers():
    pool = ThreadPool(processes=1)
    R = RSim()
    task = import_task_file()

    if result:
        failed(result)
    else:
        passed()


if __name__ == '__main__':
    run_common_tests()
    test_answers()
