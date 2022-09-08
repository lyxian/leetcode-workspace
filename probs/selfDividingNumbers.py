# A self-dividing number is a number that is divisible by every digit it contains.
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# 
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def helper(number):
            if '0' in str(number):
                return False
            else:
                for digit in str(number):
                    if number % int(digit) != 0:
                        return False
                return True
        return [i for i in range(left, right+1) if helper(i)]

if __name__ == '__main__':
    left = 1; right = 22
    # left = 47; right = 85
    print(Solution().selfDividingNumbers(left, right))