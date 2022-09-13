# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# 
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
# 
# For example, the saying and conversion for digit string "3322251":
# 
# Given a positive integer n, return the nth term of the count-and-say sequence.

class Solution:
    def countAndSay(self, n: int) -> str:
        def say(num):
            # Given string, say count then get new string/number
            numStr = curr = prev = ''
            count = 0
            for digit in str(num):
                curr = digit
                if prev:
                    if curr != prev:
                        numStr += f'{count}{prev}'
                        count = 1
                    else:
                        count += 1
                else:
                    count += 1
                prev = curr
            if count:
                numStr += f'{count}{prev}'
            # print(f'{num} -> {numStr}')
            return int(numStr)

        def helper(num):
            if num == 1:
                return 1
            elif num == 2:
                return say(1)
            else:
                return say(helper(num-1))

        return str(helper(n))
        
    def countAndSayA(self, n: int) -> str:
        import itertools
        s = "1"
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        return s

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 1
    print(Solution().countAndSayA(n))