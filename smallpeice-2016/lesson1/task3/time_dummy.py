# noinspection PyUnresolvedReferences
from time import *
import threading

sleep_called = threading.Event()
tests_done = threading.Event()


def sleep(secs):
    sleep_called.set()
    tests_done.wait(1)
    tests_done.clear()