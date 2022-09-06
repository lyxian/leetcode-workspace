# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from typing import List
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = set()
        Solution.helper(0, n, 'open', '', 0, self.ans)
        return sorted(self.ans)
    
    @staticmethod
    def helper(idx, n, action, string, counter, ans):
        if idx == 2*n:
            if counter == 0:
                ans.add(string)
        else:
            if action == 'open':
                Solution.helper(idx+1, n, 'open', string + '(', counter+1, ans)
                Solution.helper(idx+1, n, 'close', string + '(', counter+1, ans)
            else:
                if counter:
                    Solution.helper(idx+1, n, 'open', string + ')', counter-1, ans)
                    Solution.helper(idx+1, n, 'close', string + ')', counter-1, ans)

if __name__ == '__main__':
    n = 1 # ['()']
    n = 2 # ['(())', '()()']
    n = 3 # ['((()))','(()())','(())()','()(())','()()()']
    print(f'{n}: {Solution().generateParenthesis(n)}')