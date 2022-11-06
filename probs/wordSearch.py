# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Cell status
# - in word
#   - in middle
#     - search left/right
#   - at edges
#     - search to other edge
# - not in word
#   - STOP

from typing import List
class Solution:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        rows, cols = len(board), len(board[0])
        def helper(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i == rows or j < 0 or j == cols:
                return False
            else:
                if word[idx] != board[i][j]:
                    return False
                tmp = board[i][j]
                board[i][j] = ' '
                res = helper(i+1, j, idx+1) or helper(i-1, j, idx+1) or helper(i, j+1, idx+1) or helper(i, j-1, idx+1)
                board[i][j] = tmp
                return res
        for i in range(rows):
            for j in range(cols):
                if helper(i, j, 0):
                    return True
        return False
        
    def existA(self, board: List[List[str]], word: str) -> bool:
        # Get list of letters and their coordinates
        rows, cols = len(board), len(board[0])
        gridMap = {}
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in gridMap:
                    gridMap[board[i][j]] += (i,j),
                else:
                    gridMap[board[i][j]] = (i,j),
                # board[i][j] = [x[0] for x in filter(lambda x: x[1] == board[i][j], enumerate(word))]
        def isAdjacent(firstCell, secondCell):
            if abs(firstCell[0] - secondCell[0]) > 1:
                return False
            if abs(firstCell[1] -secondCell[1]) > 1:
                return False
            if abs(firstCell[0] - secondCell[0]) == 1 and abs(firstCell[1] -secondCell[1]) == 1:
                return False
            if abs(firstCell[0] - secondCell[0]) == 0 and abs(firstCell[1] -secondCell[1]) == 0:
                return False
            return True
        # return self.exist_2(gridMap, isAdjacent, word)
        return self.exist_3(gridMap, isAdjacent, word)

    def exist_3(self, gridMap, isAdjacent, word) -> bool:
        self.found = False
        def helper(currPath, idx, visited):
            if idx == len(word):
                self.found = True
                return
            if word[idx] not in gridMap:
                return False
            else:
                print(visited)
                for newPath in gridMap[word[idx]]:
                    # print(currPath, newPath, visited)
                    if newPath not in visited and isAdjacent(currPath, newPath):
                        helper(newPath, idx+1, visited+[newPath])
        if word[0] not in gridMap:
            return False
        else:
            for currPath in gridMap[word[0]]:
                helper(currPath, 1, [currPath])
        return self.found

    def exist_2(self, gridMap, isAdjacent, word) -> bool:
        print(gridMap)
        if 0:
            starting = gridMap['F'][0]
            letters = ['B', 'S']
            letters = ['A', 'B', 'C', 'E']
            for letter in letters:
                for i in gridMap[letter]:
                    print(starting, letter, i, isAdjacent(starting, i))
        currPaths = validPaths = set()
        visited = []
        for letter in word:
            if letter not in gridMap:
                if self.verbose:
                    print('letter not found')
                return False
            else:
                if currPaths:
                    newPaths = gridMap[letter]
                    for currPath in currPaths:
                        for newPath in newPaths:
                            if isAdjacent(currPath, newPath):
                                if newPath in visited:
                                    if self.verbose:
                                        print(f'{newPath} visited, skipping')
                                    continue
                                validPaths.add(newPath)
                                if not visited:
                                    visited += (word[0], currPath)
                                visited += (letter, newPath)
                    if self.verbose:
                        print(letter, validPaths)
                    if validPaths:
                        currPaths = validPaths.copy()
                        validPaths = set()
                    else:
                        if self.verbose:
                            print('no valid paths')
                        return False
                else:
                    currPaths = set(gridMap[letter])
        return True #, visited

    def exist_1(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # i = j = 0
        self.found = False
        def helper(i, j, path, visited):
            if path == word:
                # print('FOUND')
                self.found = True
                return
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if path:
                if (i, j) in visited:
                    # print(f'{path} END - visited')
                    return
                else:
                    if board[i][j] in word:
                        tmp = visited.copy()
                        tmp += (i, j),
                        helper(i+1, j, path+board[i][j], tmp)
                        helper(i-1, j, path+board[i][j], tmp)
                        helper(i, j+1, path+board[i][j], tmp)
                        helper(i, j-1, path+board[i][j], tmp)
                        return
                    else:
                        # print(f'{path} END - not found')
                        return
            else:
                if board[i][j] in word:
                    tmp = visited.copy()
                    tmp += (i, j),
                    helper(i+1, j, board[i][j], tmp)
                    helper(i-1, j, board[i][j], tmp)
                    helper(i, j+1, board[i][j], tmp)
                    helper(i, j-1, board[i][j], tmp)
                    return
                else:
                    return
        for i in range(rows):
            for j in range(cols):
                helper(i, j, '', [])
                # break
        return self.found

if __name__ == '__main__':
    # board= [["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"],["A","B","C","E","S","F","C","S","A","D","E","E"]]
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    # word = "SEE"
    # word = "ABCB"
    # word = "ABA"

    # Hidden
    # board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
    # word = "AAAAAAAAAAAAAB"
    # board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    board = [["A"]]
    word = "A"
    # board = [["a","b"],["c","d"]]
    # word = "cdba"
    print(Solution(verbose=True).exist(board, word))