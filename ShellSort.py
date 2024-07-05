import UnitTests

# Time Complexity: O(n^2) - May Improve on Insertion Sort
# Space Complexity: O(1)
# Not Stable


class ShellSort:

    def __init__(self, arr):
        self.arr = arr
        self.sort()

    def sort(self):

        # using gaps to shift over large amounts of elements together
        gap = len(self.arr) // 2

        while gap > 0:

            for i in range(gap, len(self.arr)):

                curr = self.arr[i]

                # keeps shifting items to the right as long as they're larger than the current
                j = i-1
                while j >= 0 and self.arr[j] > curr:
                    self.arr[j+1] = self.arr[j]
                    j -= 1

                # placing the current element in new location
                self.arr[j+1] = curr

            gap //= 2


UnitTests.runTestCases(ShellSort)
