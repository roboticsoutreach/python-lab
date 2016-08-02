import sr_dummy
import sys
sys.modules['sr'] = sr_dummy
import time
import threading
from Queue import Queue

from multiprocessing.pool import ThreadPool

from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


class Motor:
    def __init__(self):
        self.target = 0


class RSim:
    def __init__(self):
        self.motors = [Motor(), Motor()]


def checker(R):
    print R.motors[0].target
    print R.motors[1].target
    time.sleep(0.2)
    if abs(R.motors[0].target) != 100:
        return "The motors should be set to full power (100 and -100)"
    if R.motors[0].target != -R.motors[1].target:
        return "Motor 0 should be opposite Motor 1's power to turn on the spot"
    time.sleep(0.6)
    if R.motors[0].target == R.motors[1].target == 0:
        return ""  # Pass!
    else:
        return "Both motors should be set to 0 afterwards"


def test_answers():
    pool = ThreadPool(processes=1)
    R = RSim()
    checker_thread = pool.apply_async(checker, (R,))

    task = import_task_file()
    task.turn(R, 100, 0.5)
    result = checker_thread.get()
    if result:
        failed(result)
    else:
        passed()


if __name__ == '__main__':
    run_common_tests()
    test_answers()
