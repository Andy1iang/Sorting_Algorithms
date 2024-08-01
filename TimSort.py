# Combines Merge Sort with Insertion Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Stable


class TimSort:

    def __init__(self, arr, ascending, threshold=32):
        self.threshold = threshold
        self.ascending = ascending
        self.arr = self.sort(arr)

    def _insertionSort(self, arr):
        # first element is ignored at first
        for i in range(1, len(arr)):
            curr = arr[i]

            # keeps shifting items to the right as long as they're larger than the current
            j = i-1
            while j >= 0 and ((self.ascending and arr[j] > curr) or (not self.ascending and arr[j] < curr)):
                arr[j+1] = arr[j]
                j -= 1

            # placing the current element in new location
            arr[j+1] = curr

        return arr

    def sort(self, arr):

        # returns array when we can't split any more
        # can also use insertion sort when we split small enough
        if len(arr) <= self.threshold:
            return self._insertionSort(arr)

        # recursively splitting array
        middleIndex = len(arr) // 2
        left = arr[:middleIndex]
        right = arr[middleIndex:]

        # sorting each half
        left = self.sort(left)
        right = self.sort(right)

        # merging sorted halves
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if (self.ascending and left[i] <= right[j]) or (not self.ascending and left[i] >= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr


if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(TimSort)
