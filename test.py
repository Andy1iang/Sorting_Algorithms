import random
import time
import unitTests
    
def bogoSort(lst):
    
    if len(lst) <= 1:
        return lst
    
    temp = lst
    
    while True:
        allSorted = True
        for i in range(1,len(temp)):
            if temp[i] < temp[i-1]:
                allSorted = False
        
        if allSorted:
            return temp
        else:
            random.shuffle(temp)
            
unitTests.runTestCases(bogoSort)
