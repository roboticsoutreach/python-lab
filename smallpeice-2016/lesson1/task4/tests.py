import sr_dummy
import sys
sys.modules['sr'] = sr_dummy
from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file
import re
import threading
import os


def get_placeholder(number):
    return get_answer_placeholders()[number]

def check_motor(s, target, motor):
    placeholder = re.sub(r'#.*', '', s.strip().replace(" ", ""))
    if placeholder.startswith("[{0}].target=".format(motor)):
        if placeholder == "[{0}].target=".format(motor)+str(target):
            return ""
        else:
            return "The target needs to be {0}".format(target)
    elif placeholder.startswith("[{0}]".format(motor)):
        return "Correct motor, you need to set its 'target' value to {0}".format(target)
    elif placeholder.startswith("[{0}]".format(0 if motor == 1 else 1)):
        return "Use motor {0}, not motor {0}".format(motor, 0 if motor == 1 else 1)
    else:
        return ""


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
    if not hasattr(sr_dummy.robot.motors[0], "target") or not hasattr(sr_dummy.robot.motors[1], "target"):
        failed("You need to set the motor's 'target' value, not the motor itself!")
    if abs(sr_dummy.robot.motors[0].target) != 100:
        failed(check_motor(get_placeholder(0), 'speed', 0) or
               "You need to set motor 0 to the supplied speed before sleeping!")
    if abs(sr_dummy.robot.motors[1].target) != 100:
        failed(check_motor(get_placeholder(1), 'speed', 1) or
               "You need to set motor 1 to the supplied speed before sleeping!")
    if sr_dummy.robot.motors[0].target != - sr_dummy.robot.motors[1].target:
        failed("You need to make sure the motors are turning in opposite directions to turn on the spot.")
    time_dummy.tests_done.set()
    thread.join(1)
    if thread.isAlive():
        failed("Your code didn't finish when we expected it to...")
        os._exit(0)
    if not hasattr(sr_dummy.robot.motors[0], "target") or not hasattr(sr_dummy.robot.motors[1], "target"):
        failed("You need to set the motor's 'target' value, not the motor itself!")
    if sr_dummy.robot.motors[0].target != 0:
        failed(check_motor(get_placeholder(2), 0, 0) or "You need to stop the motor when you're done sleeping!")
    if sr_dummy.robot.motors[1].target != 0:
        failed(check_motor(get_placeholder(3), 0, 1) or "You need to stop the motor when you're done sleeping!")


if __name__ == '__main__':
    run_common_tests()
    test_answer()
