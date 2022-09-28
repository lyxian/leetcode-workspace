# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# 
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# 
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if not row or not col:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]
        return grid[-1][-1]

    def uniquePathsB(self, m: int, n: int) -> int:
        def summation(num):
            return num*(num+1)//2
        if m == 1 or n == 1:
            return 1
        elif m == 2 or n == 2:
            return m if m > n else n
        elif m == 3 or n == 3:
            return summation(m) if m > n else summation(n)
        else:
            return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)

    def uniquePathsA(self, m: int, n: int) -> int:
        self.count = 0
        def helper(row, col):
            if row > m or col > n:
                return
            elif row == m and col == n:
                self.count += 1
            else:
                helper(row+1, col)
                helper(row, col+1)
        helper(1, 1)
        return self.count

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        m, n = map(int, sys.argv[1:])
    else:
        m, n = [3, 2] # 3
        m, n = [3, 3] # 6 = 3 + 3
        m, n = [3, 4] # 10 = 6 + 4
        m, n = [3, 5] # 15 = 10 + 15
        # m, n = [3, 7] # 28

        m, n = [4, 2] # 4
        m, n = [4, 3] # 10 = 4 + 6
        m, n = [4, 4] # 20 = 10 + 10
        m, n = [4, 5] # 35 = 20 + 15

        m, n = [5, 2] # 5
        m, n = [5, 3] # 15 = 5 + 10
        m, n = [5, 4] # 35 = 15 + 20
        m, n = [5, 5] # 70 = 35 + 35

        # m, n = [20, 10]
        # m, n = [23, 12]
        # m, n = [20, 20]
    # print(Solution().uniquePathsA(m, n))
    
    print(Solution().uniquePaths(m, n))