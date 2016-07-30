from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder.contains("Robot("):
        passed("Great, now you have R as a Robot object")
    else:
        failed("Not quite, read the description and try again")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


