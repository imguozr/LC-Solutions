from collections import defaultdict
from typing import List


class Solution:
    """
        DFS.
        1. Build an adjacency list.
        2. Use set to record all the visited nodes along the way.
    """

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)

        # node_id, probability, timestamp
        dfs = [(1, 1, 0)]
        seen = set()

        while dfs:
            node, prob, time = dfs.pop()
            seen.add(node)
            if time >= t:
                if node == target:
                    return prob
                continue
            neighbour = tree[node] - seen
            for nei in neighbour or [node]:
                dfs.append((nei, prob / (len(neighbour) or 1), time + 1))

        return 0.0
