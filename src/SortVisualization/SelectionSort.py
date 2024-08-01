# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Not Stable


class SelectionSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.ascending  = ascending
        self.sort()

    def sort(self):

        # iterating through all elements of the array
        for i in range(len(self.arr)-1):
            idx = i

            # finding the minimum element of unsorted section each time
            for j in range(i, len(self.arr)):
                yield idx, j # comment out when unit testing
                if (self.ascending and self.arr[j] < self.arr[idx]) or (not self.ascending and self.arr[j] > self.arr[idx]):
                    idx = j

            # only swap if the min element is not the first
            if i != idx:
                yield i, idx # comment out when unit testing
                self.arr[i], self.arr[idx] = self.arr[idx], self.arr[i]

if __name__ == "__main__": 
    import UnitTests
    UnitTests.runTestCases(SelectionSort)
