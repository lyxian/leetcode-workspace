# The Tribonacci sequence Tn is defined as follows: 
# 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# 
# Given n, return the value of Tn.

class Solution:
    d = {
        0: 0,
        1: 1,
        2: 1,
    }

    def tribonacci(self, n: int) -> int:
        for i in range(3, n+1):
            self.d[i] = self.d[i-1] + self.d[i-2] + self.d[i-3]
        return self.d[n]
        if n in self.d:
            return self.d[n]
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

if __name__ == '__main__':
    print(Solution().tribonacci(4))
    print(Solution().tribonacci(25))
    print(Solution().tribonacci(35))