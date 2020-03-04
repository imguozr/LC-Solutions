from typing import List


class Solution:
    """
        BFS
    """

    def canReach_1(self, arr: List[int], start: int) -> bool:
        """
            Recursively.
        """

        seen = set()

        def helper(pos):
            if not 0 <= pos < len(arr) or pos in seen:
                return False
            if not arr[pos]:
                return True
            seen.add(pos)
            return helper(pos + arr[pos]) or helper(pos - arr[pos])

        return helper(start)

    def canReach_2(self, arr: List[int], start: int) -> bool:
        """
            Iteratively
        """

        from collections import deque
        queue, seen = deque([start]), {start}
        while queue:
            curr = queue.popleft()
            if not arr[curr]:
                return True
            for nxt in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= nxt < len(arr) and nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return False
