# Time Complexity: O(n^2) - May Improve on Insertion Sort
# Space Complexity: O(1)
# Not Stable


class ShellSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.ascending = ascending
        self.sort()

    def sort(self):

        # using gaps to shift over large amounts of elements together
        # checking further elements rather than neighboring elements
        gap = len(self.arr) // 2

        while gap > 0:

            for i in range(gap, len(self.arr)):

                curr = self.arr[i]

                # keeps shifting items to the right as long as they're larger than the current
                j = i-gap
                while j >= 0 and ((self.ascending and self.arr[j] > curr) or (not self.ascending and self.arr[j] < curr)):
                    self.arr[j+gap] = self.arr[j]
                    j -= gap
                    yield j+gap, i  # comment out when unit testing

                # placing the current element in new location
                self.arr[j+gap] = curr

            gap //= 2


if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(ShellSort)
