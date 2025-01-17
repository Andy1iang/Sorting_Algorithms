# TODO:
# Test for Descending order

import time
import json
import random
import signal
import copy
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
freshCase = [random.randint(0, int(1e7)) for _ in range(30)]
testCases += [["Test Case 9 (Freshly Generated List)", freshCase, sorted(freshCase), sorted(freshCase, reverse=True)]]


# used to time code
def signal_handler(signum, frame):
    raise TLE


# used to check if an array is sorted


def checkSort(arr, ascending):
    for i in range(len(arr) - 1):
        if ascending:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False

    return True


def runTestCases(sorter):

    for testCase in testCases:

        # setting up timer
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(TIME_LIMIT)

        # getting time elapsed
        start = time.time()
        # temporary line
        print(f"\033[1;33mRunning {testCase[0]} ...\033[0m", end="\r")
        try:
            descendingArr = copy.deepcopy(sorter(testCase[1], False).arr)
            ascendingArr = copy.deepcopy(sorter(testCase[1], True).arr)

        # time limit exceeded
        except TLE:
            print(" " * 50, end="\r")  # erasing the temporary line
            print(f"\u274C \033[1;31m{testCase[0]}\033[0m")
            print(f"\033[1;31mTimed out!\033[0m{' '*50}\n")

        # other types of errors:
        except Exception as e:
            print(" " * 50, end="\r")  # erasing the temporary line
            print(f"\u274C \033[1;31m{testCase[0]}\033[0m")
            print(f"\033[1;31mError: {e}\033[0m\n")

        else:
            elapsed = time.time() - start
            print(" " * 50, end="\r")  # erasing the temporary line

            # if correct
            ascendingResult = checkSort(ascendingArr, True)
            descendingResult = checkSort(descendingArr, False)
            if not ascendingResult and not descendingResult:
                print(f"\u274C \033[1;31m{testCase[0]} - Both Cases Failed\033[0m")
                print(f"Ascending - Expected: {testCase[2]}\nGot: {ascendingArr}\n")
                print(f"Descending - Expected: {testCase[3]}\nGot: {descendingArr}\n")

            elif not ascendingResult:
                print(f"\u274C \033[1;31m{testCase[0]} - Ascending Case Failed\033[0m")
                print(f"Ascending - Expected: {testCase[2]}\nGot: {ascendingArr}\n")

            elif not descendingResult:
                print(f"\u274C \033[1;31m{testCase[0]} - Descending Case Failed\033[0m")
                print(f"Descending - Expected: {testCase[3]}\nGot: {descendingArr}\n")

            else:
                print(f"\u2705 \033[1;32m{testCase[0]} - Both Cases Passed\033[0m")
                print(formatTime(elapsed) + "\n")


def formatTime(elapsed):
    resFormat = "Code Executed in: "

    # formatting the seconds & converting units to be more readable
    if elapsed < 0.000001:
        return f"{resFormat}{elapsed*1000000:.3f} Microseconds"
    elif elapsed < 0.001:
        return f"{resFormat}{elapsed*1000:.3f} Milliseconds"
    else:
        return f"{resFormat}{elapsed:.3f} Seconds"
