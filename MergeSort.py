import UnitTests

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Stable


class MergeSort:

    def __init__(self, arr, ascending):
        self.arr = self.sort(arr)
        self.ascending  = ascending

    def sort(self, arr):

        # returns array when we can't split any more
        # can also use insertion sort when we split small enough
        if len(arr) <= 1:
            return arr

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
            if (self.ascending and left[i] <= right[j]) or (self.ascending and left[i] >= right[j]):
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


UnitTests.runTestCases(MergeSort)
