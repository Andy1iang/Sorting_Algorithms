# Integer Only (Expecting Test Case 8 to Fail)
# Time Complexity: O(n+k) - Only efficient when there's minimal variation in elements
# k = maximum minus minimum key values
# Space Complexity: O(k)
# Stable


class CountingSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.ascending = ascending
        if len(arr) > 1:  # only sorting if there's something to sort
            self.counts = [0]*((max(arr)-min(arr))+1)
            self.sort()

    def sort(self):
        # getting minimum of array first
        minNum = min(self.arr)

        # storing the counts of all original elements in a new array
        for num in self.arr:
            self.counts[num - minNum] += 1

        # accessing the new array and overwriting the original array in sorted order
        c = 0
        for i in range(len(self.counts)):
            b = c # to keep track of the current green for visualizer

            # if we want to sort by descending order
            if not self.ascending:
                i = len(self.counts) - i - 1

            # keeps adding the same elements as needed (overwriting original array)
            while self.counts[i] > 0:
                self.arr[c] = i + minNum
                c += 1
                self.counts[i] -= 1
                yield b, c # comment out when unit testing

if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(CountingSort)
