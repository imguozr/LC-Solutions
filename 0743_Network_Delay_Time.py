import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime1(self, times: List[List[int]], N: int, K: int) -> int:
        """
            DFS
        """
        # build adjacent list
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            dist[node] = time
            for neib, t in sorted(graph[node]):
                dfs(neib, time + t)

        dfs(K, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1

    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        """
            Dijkstra
        """
        # build adjacent list
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # store all nodes and its distance to K we met
        heap = [(0, K)]
        # keep track of distance of every nodes to K
        dist = {}

        while heap:
            # break if all distances has been determined (unnecessary)
            if len(dist) == N:
                break
            d, node = heapq.heappop(heap)
            # go for next if distance has been determined before (unnecessary)
            if node in dist:
                continue
            dist[node] = d
            # check neighbors of node
            for neib, d2 in graph[node]:
                # pass determined neighbors
                if neib not in dist:
                    heapq.heappush(heap, (d + d2, neib))

        # if not all nodes are visited return -1 else return max value
        return max(dist.values()) if len(dist) == N else -1
