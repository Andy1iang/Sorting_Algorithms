# Time Complexity: O(n^2) - Speeds up when original array is close to sorted
# Space Complexity: O(1)
# Stable


class InsertionSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.ascending = ascending
        self.sort()

    def sort(self):

        # first element is ignored at first
        for i in range(1, len(self.arr)):
            curr = self.arr[i]

            # keeps shifting items to the right as long as they're larger than the current
            j = i-1
            while j >= 0 and ((self.ascending and self.arr[j] > curr) or (not self.ascending and self.arr[j] < curr)):
                self.arr[j+1] = self.arr[j]
                j -= 1
                yield j+1, i  # comment out when unit testing

            # placing the current element in new location
            self.arr[j+1] = curr


if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(InsertionSort)
