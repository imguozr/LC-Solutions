class Solution:
    """
    The intuition is to find the longest common prefix of given numbers.

    1. Find common prefix by shift numbers to right
    2. Restore result by shift start number to left
    """

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m < n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift
