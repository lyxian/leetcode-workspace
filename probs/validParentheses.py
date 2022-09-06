# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        toClose = []
        closing = '}])'
        pairMapping = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for i in s:
            # print(i, ':', *toClose)
            if i in closing:
                if toClose:
                    if pairMapping[i] != toClose[-1]:
                        return False
                    else:
                        toClose.pop()
                else:
                    return False
            else:
                toClose.append(i)
        return len(toClose) == 0

if __name__ == '__main__':
    # s = '()[]'
    # s = '({})[]'
    s = '({((()))})'
    print(f's = {s} | {Solution().isValid(s)}')