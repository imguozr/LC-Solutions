from typing import List


class Solution:
    """
        Record the rightest lighting light R.
        If all the lights before R is blue or on (Pointer reach the light before R),
        res += 1
    """

    def numTimesAllBlue(self, light: List[int]) -> int:
        right = res = 0
        for i, l in enumerate(light):
            # Update right
            right = max(right, l)
            if right == i + 1:
                res += 1
        return res
