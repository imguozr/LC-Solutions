from typing import List


class Solution:
    def minCost_1(self, grid: List[List[int]]) -> int:
        """
            Dijsktra algorithm using priority queue.
        """
        import heapq

        m, n = len(grid), len(grid[0])
        dist = [0] + [10 ** 9] * (m * n - 1)
        seen = set()
        queue = [(0, 0, 0)]

        while queue:
            curr_dis, x, y = heapq.heappop(queue)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            curr_pos = x * n + y

            for i, (a, b) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_pos = a * n + b
                new_dis = dist[curr_pos] + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= a < m and 0 <= b < n and new_dis < dist[new_pos]:
                    dist[new_pos] = new_dis
                    heapq.heappush(queue, (new_dis, a, b))

        return dist[-1]

    def minCost_2(self, grid: List[List[int]]) -> int:
        """
            BFS iteratively.
        """
        import collections

        m, n = len(grid), len(grid[0])
        dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue, costs = collections.deque([(0, 0, 0)]), {}

        while queue:
            cost, nxt_x, nxt_y = queue.popleft()
            while 0 <= nxt_x < m and 0 <= nxt_y < n and (nxt_x, nxt_y) not in costs:
                costs[(nxt_x, nxt_y)] = cost
                queue += [(cost + 1, nxt_x + dx, nxt_y + dy) for dx, dy in dire]
                dx, dy = dire[grid[nxt_x][nxt_y] - 1]
                nxt_x, nxt_y = nxt_x + dx, nxt_y + dy

        return costs[(m - 1, n - 1)]

    def minCost_3(self, grid: List[List[int]]) -> int:
        """
            0-1 BFS
        """
        import collections
        import math
        from typing import Iterator, Tuple

        m, n = len(grid), len(grid[0])

        # Iterate over the neighborhood of a position in the grid.
        # Only neighbors within the grid boundaries are yielded.
        # The cost to visit the neighbor is 0 if the current positions
        # sign points to the neighbor. Otherwise it is 1.
        def neighborhood(y: int, x: int) -> Iterator[Tuple[int, int, int]]:
            if x + 1 < n:
                yield y, x + 1, int(grid[y][x] != 1)
            if x > 0:
                yield y, x - 1, int(grid[y][x] != 2)
            if y + 1 < m:
                yield y + 1, x, int(grid[y][x] != 3)
            if y > 0:
                yield y - 1, x, int(grid[y][x] != 4)

        # The initial cost to visit a node is infinity.
        # Only the start node can be reached with a cost of 0.
        min_cost = collections.defaultdict(lambda: math.inf, {(0, 0): 0})
        queue = collections.deque([(0, 0, 0)])

        while queue:
            cost, y, x = queue.popleft()

            # We can skip queue entries if we have already found a more
            # efficient path to their position.
            if cost != min_cost[y, x]:
                continue

            # The target position has been found and we can return the cost.
            if y == m - 1 and x == n - 1:
                return cost

            # Visit the neighbors of the current position if the path over the
            # current node improves the minimum cost to reach them.
            for y2, x2, step_cost in neighborhood(y, x):
                cost2 = cost + step_cost
                if cost2 < min_cost[y2, x2]:
                    min_cost[y2, x2] = cost2

                    # Append a neighbor to the left of the queue if there is
                    # no additional step cost. Otherwise append the neighbor
                    # to the right.
                    if not step_cost:
                        queue.appendleft((cost2, y2, x2))
                    else:
                        queue.append((cost2, y2, x2))

        return 0
