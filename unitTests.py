import time
import json
import random
import signal
from typing import Callable

with open("Test_Cases.json", "r") as tst:
        testCases = json.load(tst)   
tst.close()

freshCase = [random.randint(0,int(1E5)) for _ in range(30)]
testCases += [["Test Case 8 (Freshly Generated List)",freshCase,sorted(freshCase)]] #??


def signal_handler(signum, frame):
    raise Exception("Timed out!")

def runTestCases(sorter: Callable) -> None:
    
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(15)

    try:
        for testCase in testCases:
            start = time.time() # add time taken
            print(f'Running {testCase[0]} ...', end ='\r')
            if testCase[2] == sorter(testCase[1]):
                print(f'\u2705 \033[1;32m{testCase[0]}\033[0m{' '*100}')
            else:
                print(f'\u274C \033[1;31m{testCase[0]}\033[0m{' '*100}')
        
    except Exception:
        print(f"Timed out!{' '*100}")



    
    
    

# for i in range(6):
#     print(f"Running Test Case 1 {'.'*(i%3+1)}   ",end='\r')
#     time.sleep(1)


def generateTestCases():
    
    longList = random.sample(list(range(int(1E5))),int(1E3))
    largeList = random.sample(list(range(int(1E5),int(1E8),int(1E3))),50)
    
    testCases = [
    ["Test Case 1 (Empty List)", [],[]],
    ["Test Case 2 (Single Element List)", [1],[1]],
    ["Test Case 3 (Uniform List)", [0]*100,[0]*100],
    ["Test Case 4 (Ordered List)", list(range(100)),list(range(100))],
    ["Test Case 4 (Reversed List)", list(range(100,0,-1)),list(range(1,101))],
    ["Test Case 5 (Long List)", longList, sorted(longList)],
    ["Test Case 6 (Large Elements List)", largeList, sorted(largeList)],
    ["Test Case 7 (Strange Elements List)", [0,-50,1E9,5.55,0b11011000,0o12,0x12], sorted([0,-50,1E9,5.55,0b11011000,0o12,0x12])],
    ]

    with open("Test_Cases.json","w") as f:
        json.dump(testCases, f)