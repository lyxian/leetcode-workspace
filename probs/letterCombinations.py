# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digit > digit > ..
        digitMapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n = len(digits)
        self.combinations = []
        def helper(idx, letters):
            if idx == n:
                self.combinations += [letters]
                return
            else:
                for letter in digitMapping[digits[idx]]:
                    helper(idx+1, letters + letter)
        if digits == '':
            return []
        else:
            helper(0, '')
            return self.combinations

if __name__ == '__main__':
    digits = '23'
    digits = '2345'
    # print(Solution().letterCombinations(digits))
    print(sorted(Solution().letterCombinations(digits)))