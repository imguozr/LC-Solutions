"""
    N queens problem is to set N queens on a N * N board,
    making each queen cannot attack the others.

    This is a permutation problem.
    We can use DFS or Backtracking to solve it.
"""
from typing import List


class Solution1:
    """
        Backtracking
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        res, board = [], [['.'] * n for _ in range(n)]
        self.backtrack(board, 0, res)
        return res

    def backtrack(self, board, row, res):
        if row == len(board):
            tmp_res = []
            for _ in board:
                tmp = ''.join(_)
                tmp_res.append(tmp)
            res.append(tmp_res)
            return
        for col in range(len(board[0])):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1, res)
            board[row][col] = '.'

    def is_valid(self, board, row, col):
        n = len(board)
        # not in same column
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        # not in same line y = x + b
        up_row, up_col = row, col
        while up_row > 0 and up_col < n - 1:
            up_row -= 1
            up_col += 1
            if board[up_row][up_col] == 'Q':
                return False
        # not in same line y = -x + b
        down_row, down_col = row, col
        while down_row > 0 and down_col > 0:
            down_row -= 1
            down_col -= 1
            if board[down_row][down_col] == 'Q':
                return False
        return True


class Solution2:
    """
        Depth First Search.
        We should notice that multiple queens in 2 lines with slope of 45 or 135 are not allowed.
        Which means in the line y - x = b or line y + x = s should only appears one queen.

        List queens represents each queen's location.
        E.g. [1, 3, 0, 2] means: Queen on row 0 locates at column 1,
        Queen on row 1 locates at column 3, and so on.
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens=[], xy_diff=[], xy_sum=[]):
            length = len(queens)
            if length == n:
                res.append(queens)
                return

            for q in range(n):
                if q not in queens and \
                        length - q not in xy_diff and \
                        length + q not in xy_sum:
                    dfs(queens + [q], xy_diff + [length - q], xy_sum + [length + q])

        res = []
        dfs()
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in seq] for seq in res]
