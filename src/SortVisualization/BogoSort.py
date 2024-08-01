from random import shuffle

# Time Complexity: O(n!) - average case
# Space Complexity: O(1)
# Not Stable


class BogoSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.ascending = ascending
        self.sort()

    # function to check whether the array is sorted
    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if (self.ascending and arr[i] < arr[i-1]) or (not self.ascending and arr[i] > arr[i-1]):
                return False
        return True

    # keep shuffling array until sorted
    def sort(self):
        while not self.isSorted(self.arr):
            shuffle(self.arr)
            yield None # comment out when unit testing

if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(BogoSort)
