# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# 
# Given an integer n, return true if n is an ugly number.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            primes = [2, 3, 5]
            while primes:
                if n % primes[0] == 0:
                    n /= primes[0]
                else:
                    primes.pop(0)
            return n == 1

if __name__ == '__main__':
    n = 5
    print(Solution().isUgly(n))