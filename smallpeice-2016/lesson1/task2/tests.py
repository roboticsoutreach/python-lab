import sr_dummy
import sys
sys.modules['sr'] = sr_dummy
from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


def test_answer_placeholders():
    task = import_task_file()
    if hasattr(task, "R") and isinstance(task.R, sr_dummy.Robot):
        passed("Great, now you have R as a Robot object")
    else:
        failed("Not quite, read the description and try again")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
