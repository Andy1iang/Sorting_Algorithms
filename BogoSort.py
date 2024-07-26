from random import shuffle
import UnitTests

# Time Complexity: O(n!) - average case
# Space Complexity: O(1)
# Not Stable


class BogoSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.sort()

    # function to check whether the array is sorted
    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True

    # keep shuffling array until sorted
    def sort(self):
        while not self.isSorted(self.arr):
            shuffle(self.arr)
            yield None

if __name__ == "__main__":
    UnitTests.runTestCases(BogoSort)
