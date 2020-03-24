from typing import List


class Solution:
    """
    DFS
    """

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if not grid or not grid[0]:
            return False

        m, n = len(grid), len(grid[0])
        # Most important
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        seen = set()
        goal = (m - 1, n - 1)

        def dfs(i, j):
            seen.add((i, j))
            if (i, j) == goal:
                return True
            for a, b in directions[grid[i][j]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen and \
                        (-a, -b) in directions[grid[x][y]]:  # connected with previous cell
                    if dfs(x, y):
                        return True
            return False

        return dfs(0, 0)
