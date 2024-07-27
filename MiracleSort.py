# Time Complexity: O(1) - With Divine Intervention
# Space Complexity: O(1)
# Stable-ish


class MiracleSort:

    def __init__(self, arr, ascending):
        self.arr = arr
        self.ascending = ascending
        self.sort()

    # keep just keep looping through until we are sorted
    def sort(self):
        while True:
            sorted = True
            for i in range(len(self.arr) - 1):
                yield i, i+1 # comment out when unit testing
                if (self.ascending and self.arr[i] > self.arr[i + 1]) or (not self.ascending and self.arr[i] < self.arr[i + 1]):
                    sorted = False

            # when divine intervention happens
            if sorted:
                return True


if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(MiracleSort)
