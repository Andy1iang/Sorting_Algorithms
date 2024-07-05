import time
import json
import random
import signal
from typing import Callable

# time limit for each test case (in seconds)
TIME_LIMIT = 15

# used to throw Time Limit Exceeded Exceptions


class TLE(Exception):
    def __init__(self):
        super(TLE, self).__init__()


# loading pre-written test cases
with open("Test_Cases.json", "r") as tst:
    testCases = json.load(tst)
tst.close()

# generating a new test case
freshCase = [random.randint(0, int(1E7)) for _ in range(30)]
testCases += [["Test Case 9 (Freshly Generated List)",
               freshCase, sorted(freshCase)]]


# used to time code
def signal_handler(signum, frame):
    raise TLE


def runTestCases(sorter):
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(TIME_LIMIT)

    try:
        for testCase in testCases:

            # getting time elapsed
            start = time.time()
            # temporary line
            print(f'\033[1;33mRunning {testCase[0]} ...\033[0m', end='\r')
            testObject = sorter(testCase[1])
            print(' '*50, end='\r')  # erasing the temporary line
            elapsed = time.time() - start

            # if correct
            if testCase[2] == testObject.arr:
                print(f'\u2705 \033[1;32m{testCase[0]}\033[0m')
                print(formatTime(elapsed)+"\n")

            # if incorrect
            else:
                print(f'\u274C \033[1;31m{testCase[0]}\033[0m')
                print(f"Expected: {testCase[2]}\nGot: {testObject.arr}\n")

    # time limit exceeded
    except TLE:
        print(f"\033[1;31mTimed out!\033[0m{' '*50}")

    # other types of errors:
    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")


def formatTime(elapsed):
    resFormat = 'Code Executed in: '

    # formatting the seconds & converting units to be more readable
    if elapsed < 0.000001:
        return f'{resFormat}{elapsed*1000000:.3f} Microseconds'
    elif elapsed < 0.001:
        return f'{resFormat}{elapsed*1000:.3f} Milliseconds'
    else:
        return f'{resFormat}{elapsed:.3f} Seconds'
