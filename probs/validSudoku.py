# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# 
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check horizontal
        def uniqueCells(array):
            return len(set(array)) == len(array)
        for row in board:
            array = [i for i in row if i != '.']
            if not uniqueCells(array):
                if self.verbose:
                    print('bad row', array)
                return False
        # Check vertical
        for idx in range(9):
            array = [row[idx] for row in board if row[idx] != '.']
            if not uniqueCells(array):
                if self.verbose:
                    print('bad column', array)
                return False
        # Check 3x3
        for rowIdx in range(3):
            for colIdx in range(3):
                array = [col for row in board[rowIdx*3:rowIdx*3 + 3] for col in row[colIdx*3:colIdx*3 + 3] if col != '.']
                if not uniqueCells(array):
                    if self.verbose:
                        print('bad 3x3', rowIdx, colIdx, array)
                    return False
        return True

    def __init__(self, verbose=False):
        self.verbose = verbose

if __name__ == '__main__':
    board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(Solution(True).isValidSudoku(board))