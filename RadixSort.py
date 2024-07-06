import UnitTests

# Integer only (Can be edited to handle ASCII) - Test 8 Not Excepted to Work
# Time Complexity: O(n*d)
# d is the amount of digits in the largest number
# Space Complexity: O(n+d)
# Stable

BUCKETS = 10


class RadixSort:

    def __init__(self, arr):
        self.arr = arr
        if len(self.arr) > 1:
            self.sort()

    def getDigits(self, num):
        return len(str(num))

    def countingSort(self, digit):
        # avoid using [[]]*BUCKETS due to shallow copying
        counts = [[] for _ in range(BUCKETS)]

        # sorting the numbers based the digit we are currently on

        # putting the numbers in the buckets
        for num in self.arr:
            idx = (num // (BUCKETS ** digit)) % BUCKETS
            counts[idx].append(num)

        # editing the array based on the counts in the buckets
        i = 0
        for bucket in counts:
            while len(bucket) > 0:
                self.arr[i] = bucket.pop(0)
                i += 1

    def sort(self):
        # Least Significant Digit Approach
        for digit in range(self.getDigits(max(self.arr))):
            self.countingSort(digit)


UnitTests.runTestCases(RadixSort)
