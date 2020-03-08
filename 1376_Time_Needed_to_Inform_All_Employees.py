from typing import List


class Solution:
    """
        DFS & DP.
        time[employee] = time[manager] + inform_time[manager]
    """

    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        if n == 1:
            return 0

        relation = {}
        for i, m in enumerate(manager):
            if m in relation:
                relation[m].append(i)
            else:
                relation[m] = [i]

        stack = [(head_id, relation[head_id])]
        time = [0] * n
        while stack:
            leader, lst = stack.pop()
            for man in lst:
                time[man] = time[leader] + inform_time[leader]
                if man in relation:
                    stack.append((man, relation[man]))
        return max(time)
