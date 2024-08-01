# Time Complexity: O(n^2) - average & worst case
# Space Complexity: O(1)
# Stable


class BubbleSort:

    def __init__(self, arr, ascending=True):
        self.arr = arr
        self.ascending = ascending
        self.sort()

    def sort(self):

        if len(self.arr) <= 1:
            return

        for i in range(len(self.arr)):

            # keeping track of if any swaps have been made in the current iteration
            swapped = False

            # loop to compare self.arr elements
            # each iteration guarantees one more element at the end to be sorted
            for j in range(0, len(self.arr) - i - 1):

                # compare two adjacent elements
                # change > to < to sort in descending order
                if (self.ascending and self.arr[j] > self.arr[j + 1]) or (not self.ascending and self.arr[j] < self.arr[j + 1]):

                    # swapping the items
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True
                    yield j, j+1  # comment out when unit-testing

            # if nothing has been swapping, we can end the program
            if swapped is False:
                break


if __name__ == "__main__":
    import UnitTests
    UnitTests.runTestCases(BubbleSort)
