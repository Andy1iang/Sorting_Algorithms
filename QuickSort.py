# Time Complexity: O(nlogn) - Worst Case: O(n^2)
# Space Complexity: O(1)
# Not Stable


class QuickSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.ascending = ascending
        self.sort()

    def sort(self):
        self._sort(0, len(self.arr)-1)

    # recursive function
    # sort by getting all pivot elements to their correct index
    def _sort(self, low, high):

        # Base Case: when there's not enough elements to sort
        if low >= high:
            return

        pivotIndex = self.partition(low, high)  # partitioning
        self._sort(low, pivotIndex-1)
        self._sort(pivotIndex+1, high)

    def partition(self, low, high):

        # creating pivot element
        pivot = (low+high)//2
        pivotValue = self.arr[pivot]
        self.swap(pivot, high)  # swapping it to the end temporarily

        # checking all elements in the subsection until pivot is is it's correct location
        # where all items to the left are smaller and to the right are larger
        i = low
        for j in range(low, high):
            if (self.ascending and self.arr[j] < pivotValue) or (not self.ascending and self.arr[j] > pivotValue):
                self.swap(i, j)
                i += 1

        self.swap(i, high)
        return i

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(QuickSort)
