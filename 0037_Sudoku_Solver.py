from typing import List


class Solution:
    """
        Backtracking.
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def solve():
            if not unoccupied:
                return
            tmp = (-1, -1)
            choices = {str(_) for _ in range(1, 10)}

            for row, col in unoccupied:
                possible_moves = rows[row].intersection(cols[col]).intersection(boxes[(row // 3) * 3 + col // 3])
                if not possible_moves:
                    return
                elif len(possible_moves) < len(choices):
                    tmp = (row, col)
                    choices = possible_moves

            for choice in choices:
                if unoccupied:
                    row, col = tmp
                    unoccupied.remove((row, col))
                    board[row][col] = choice
                    rows[row].remove(choice)
                    cols[col].remove(choice)
                    boxes[(row // 3) * 3 + col // 3].remove(choice)

                    solve()

                    # not a valid answer, backtrack
                    if unoccupied:
                        unoccupied.add((row, col))
                        board[row][col] = '.'
                        rows[row].add(choice)
                        cols[col].add(choice)
                        boxes[(row // 3) * 3 + col // 3].add(choice)

        if not board or not board:
            return
        # available # to fill in the cell
        rows = [{str(_) for _ in range(1, 10)} for _ in range(9)]
        cols = [{str(_) for _ in range(1, 10)} for _ in range(9)]
        boxes = [{str(_) for _ in range(1, 10)} for _ in range(9)]
        # cells need to fill
        unoccupied = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    unoccupied.add((i, j))
                else:
                    val = board[i][j]
                    rows[i].remove(val)
                    cols[j].remove(val)
                    boxes[(i // 3) * 3 + j // 3].remove(val)
        solve()
