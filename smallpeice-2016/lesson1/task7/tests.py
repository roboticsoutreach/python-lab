import sr_dummy
import sys
sys.modules['sr'] = sr_dummy

from test_helper import passed

if __name__ == '__main__':
    passed("There are no tests for this task!")


