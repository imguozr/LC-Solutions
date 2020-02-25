class Solution:
    """
        Similar with # 733.
        https://mp.weixin.qq.com/s/Y7snQIraCC6PRhj9ZSnlzw
    """

    def colorBorder_1(self, grid: list[list[int]], r0: int, c0: int, color: int) -> list[list[int]]:
        """
            DFS
        """
        seen = set()
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if (x, y) in seen:
                return True
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == grid[r0][c0]):
                return False
            seen.add((x, y))
            if dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1) < 4:
                grid[x][y] = color
            return True

        dfs(r0, c0)
        return grid

    def colorBorder_2(self, grid: list[list[int]], r0: int, c0: int, color: int) -> list[list[int]]:
        """
            BFS 1
        """
        stack, component, border = [(r0, c0)], {(r0, c0)}, set()
        m, n = len(grid), len(grid[0])

        for r, c in stack:
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x, y = r + i, c + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] == grid[r][c]:
                    if (x, y) not in component:
                        stack.append((x, y))
                        component.add((x, y))
                else:
                    border.add((r, c))
        for x, y in border:
            grid[x][y] = color
        return grid

    def colorBorder_3(self, grid: list[list[int]], r0: int, c0: int, color: int) -> list[list[int]]:
        """
            BFS 2. Color border directly.
        """
        from collections import deque
        queue, component = deque([(r0, c0)]), {(r0, c0)}
        m, n = len(grid), len(grid[0])
        clr = grid[r0][c0]

        while queue:
            r, c = queue.popleft()
            if not r * c * (r - m + 1) * (c - n + 1):
                grid[r][c] = color

            for i, j in [0, 1], [0, -1], [1, 0], [-1, 0]:
                x, y = r + i, c + j
                if 0 <= x < m and 0 <= y < n and (x, y) not in component:
                    if grid[x][y] == clr:
                        queue.append((x, y))
                        component.add((x, y))
                    else:
                        grid[r][c] = color
        return grid
