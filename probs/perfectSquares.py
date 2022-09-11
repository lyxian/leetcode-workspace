# Given an integer n, return the least number of perfect square numbers that sum to n.
# 
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

class Solution:
    showArray = True
    def numSquares(self, n: int) -> int:
        # Breadth-First Search
        if n < 4:
            return n
        def helper(n):
            depth = 0
            array = [n]
            while True:
                depth += 1
                nextArray = []
                for num in array:
                    lastSquare = int(num**0.5)
                    for i in range(1, lastSquare+1)[::-1]:
                        if num == i ** 2:
                            return depth
                        if num >= i ** 2:
                            nextArray += [num - i**2]
                array = nextArray
        return helper(n)

    def numSquaresB(self, n: int) -> int:
        # Depth-First Search
        self.array = []
        def helper(num, count):
            if num < 0:
                return
            elif num == 0 :
                self.array.append(count)
            else:
                previousSquare = int(num**0.5)
                for i in range(1, previousSquare+1)[::-1]:
                    if num % i == 0:
                        self.array.append(count + int(num / i**2))
                    else:
                        helper(num - i**2, count+1)
        lastSquare = int(n**0.5)
        for i in range(1, lastSquare+1)[::-1]:
            if n % i == 0:
                self.array.append(int(n / i**2))
            else:
                helper(n-i**2, 1)
        return self.array

    def numSquaresA(self, n: int) -> int:
        # naive
        def helper(num, array):
            if num == 0:
                return 
            else:
                previousSquare = int(num**0.5)
                array.append(previousSquare**2)
                return helper(num - previousSquare**2, array)
        array = []
        helper(n, array)
        return array

if __name__ == '__main__':
    import sys
    # sys.setrecursionlimit(1500)
    n = 12
    n = 13
    n = int(sys.argv[1])
    print(Solution().numSquares(n))