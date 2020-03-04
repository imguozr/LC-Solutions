import math
from typing import List


class Solution:
    """
        I dont know what the algorithm is...
    """

    def closestDivisors(self, num: int) -> List[int]:
        def helper(n):
            s = int(math.sqrt(n) // 1)
            for v1 in range(s, 1, -1):
                v2 = n // v1
                if not n % v1 and not n % v2:
                    return [v1, v2]
            return [1, n]

        div1 = helper(num + 1)
        div2 = helper(num + 2)
        return div1 if div1[1] - div1[0] < div2[1] - div2[0] else div2
