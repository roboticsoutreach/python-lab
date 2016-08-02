import sr_dummy
import sys
sys.modules['sr'] = sr_dummy
from test_helper import run_common_tests, failed, passed, get_answer_placeholders
import re


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


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    err_string = check_motor(placeholders[0], 100)
    if err_string:
        failed("Line 10:" + err_string)

    err_string = check_motor(placeholders[1], 0)
    if err_string:
        failed("Line 17:" + err_string)
    else:
        passed("Good Job!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
