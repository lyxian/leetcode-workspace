# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def helper(num):
            if num == 1:
                return '1'
            else:
                return helper(num-1) + bin(num)[2:]
        return int(helper(n), 2) % (10**9 + 7)

    def concatenatedBinaryB(self, n: int) -> int:
        # Get binary string > Convert to decimal
        s = ''
        for i in range(n):
            s += bin(i+1)[2:]
        return int(s, 2) % (10**9 + 7)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        n = 1
    else:
        n = int(sys.argv[1])
        sys.setrecursionlimit(n*10)
    print(Solution().concatenatedBinary(n))