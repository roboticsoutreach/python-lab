import sr_dummy
import sys
sys.modules['sr'] = sr_dummy
from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file
import re
import threading
import os


def get_placeholder(number):
    return get_answer_placeholders()[number]

def check_motor(s, target):
    placeholder = re.sub(r'#.*', '', s.strip().replace(" ", ""))
    if placeholder.startswith("[0].target="):
        if placeholder == "[0].target="+str(target):
            return ""
        else:
            return "The target needs to be {0}".format(target)
    elif placeholder.startswith("[0]"):
        return "Correct motor, you need to set its 'target' value to {0}".format(target)
    elif placeholder.startswith("[1]"):
        return "Use motor 0, not motor 1"
    else:
        return "Something's not right with m[0]"


def test_answer():
    import time_dummy
    sys.modules['time'] = time_dummy
    thread = threading.Thread(target=import_task_file)
    thread.start()
    if not time_dummy.sleep_called.wait(1):
        failed("You need to call time.sleep!")
    time_dummy.sleep_called.clear()
    if not sr_dummy.robot:
        failed("You should create a robot before sleeping!")
    if not hasattr(sr_dummy.robot.motors[0], "target"):
        failed("You need to set the motor's 'target' value, not the motor itself!")
    if sr_dummy.robot.motors[0].target != 100:
        failed(check_motor(get_placeholder(0), 100) or "You need to set motor 0 to 100 before sleeping!")
    time_dummy.tests_done.set()
    thread.join(1)
    if thread.isAlive():
        failed("Your code didn't finish when we expected it to...")
        os._exit(0)
    if not hasattr(sr_dummy.robot.motors[0], "target"):
        failed("You need to set the motor's 'target' value, not the motor itself!")
    if sr_dummy.robot.motors[0].target != 0:
        failed(check_motor(get_placeholder(1), 0) or "You need to stop the motor when you're done sleeping!")


if __name__ == '__main__':
    run_common_tests()
    test_answer()
