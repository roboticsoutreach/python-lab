import sr_dummy
import sys
sys.modules['sr'] = sr_dummy
from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder.startswith("sr import *"):
        passed("Good job!")
    else:
        if "sr import" in placeholder:
            failed("You should not use anything other than * when importing Student Robotics code")
        else:
            failed("Check the task description, this isn't quite right!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


