from collections import defaultdict
from typing import List


class Solution:
    """
        Intuition: if (0, 1) and (0, 2) are two exchange pairs, then any 2 items in (0, 1, 2) can be exchanged.
    """

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionFind:
            """
                Union Find Algorithm.
            """

            def __init__(self, n):
                self.pairs = list(range(n))

            def find(self, p):
                if p != self.pairs[p]:
                    self.pairs[p] = self.find(self.pairs[p])
                return self.pairs[p]

            def union(self, p, q):
                a = self.find(p)
                b = self.find(q)
                if b < a:
                    a, b = b, a
                self.pairs[b] = a

        uf, res, memo = UnionFind(len(s)), [], defaultdict(list)
        for p, q in pairs:
            uf.union(p, q)

        # Add char to memo dict.
        for i, ch in enumerate(s):
            idx = uf.find(i)
            memo[idx].append(ch)
        for key in memo.keys():
            memo[key].sort(reverse=True)

        # Generate answer by pop char out of memo.
        for i in range(len(s)):
            idx = uf.find(i)
            ch = memo[idx].pop()
            res.append(ch)

        return ''.join(res)
