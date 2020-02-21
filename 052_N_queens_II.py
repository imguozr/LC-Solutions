class Solution:
    """
        Return count is fine.
        No need to generate game board.
    """

    def totalNQueens(self, n: int) -> int:
        return self.backtrack(n, set(), set(), set(), 0)

    def backtrack(self, n, xy_dif, xy_sum, q_col, row):
        if row == n:
            return 1

        res = 0
        for col in range(n):
            if col in q_col or col + row in xy_sum or row - col in xy_dif:
                continue

            xy_dif.add(row - col)
            xy_sum.add(row + col)
            q_col.add(col)

            res += self.backtrack(n, xy_dif, xy_sum, q_col, row + 1)

            xy_dif.remove(row - col)
            xy_sum.remove(row + col)
            q_col.remove(col)

        return res
