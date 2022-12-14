# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
# 
# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
# 
# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
# 
# Return the maximum number of points you can achieve.
# 
# abs(x) is defined as:
# 
# x for x >= 0.
# -x for x < 0.

from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Update each row with total points > return max points
        rows = len(points)
        cols = len(points[0])
        for row in range(1, rows):
            leftArray = [0] + [0] * cols
            for col in range(cols):
                leftArray[col+1] = max(points[row-1][col], leftArray[col] - 1)
            rightArray = [0] * cols + [0]
            for col in range(cols-1, -1, -1):
                rightArray[col] = max(points[row-1][col], rightArray[col+1] - 1)
            for col in range(cols):
                points[row][col] += max(leftArray[col+1], rightArray[col])
        return max(points[-1])

    def maxPointsA(self, points: List[List[int]]) -> int:
        # Update each row with total points > return max points
        rows = len(points)
        cols = len(points[0])
        for row in range(1, rows):
            for col in range(cols):
                points[row][col] = max([points[row][col] + val - abs(idx - col) for idx, val in enumerate(points[row-1])])
        return max(points[-1])

if __name__ == '__main__':
    points = [[1,2,3],[1,5,1],[3,1,1]]
    # points = [[1,5],[2,3],[4,2]]
    # points = [[56,26,7,247,835,2,34,134,123,1,3,213],[56,26,7,247,835,2,34,134,123,1,3,213],[56,26,7,247,835,2,34,134,123,1,3,213],[56,26,7,247,835,2,34,134,123,1,3,213]]
    print(Solution().maxPoints(points))