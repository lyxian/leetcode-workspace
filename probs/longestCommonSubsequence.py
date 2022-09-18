# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# 
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# 
# For example, 'ace' is a subsequence of 'abcde'.
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        grid = [[0 for _ in range(1+n2)] for _ in range(1+n1)] # n2 = cols , n2 = rows
        for idx1 in range(1,n1+1):
            for idx2 in range(1,n2+1):
                if text1[idx1-1] == text2[idx2-1]:
                    grid[idx1][idx2] = 1 + grid[idx1-1][idx2-1]
                else:
                    grid[idx1][idx2] = max(grid[idx1][idx2-1],grid[idx1-1][idx2])
        if self.verbose:
            print(' ', *text2)
            for row in range(1,len(grid)):
                print(text1[row-1], *grid[row][1:])
        return grid[-1][-1]

    def longestCommonSubsequenceA(self, text1: str, text2: str) -> int:
        # uncommon2 = {ord(letter): '' for letter in text2 if letter not in text1}
        # text2 = text2.translate(uncommon2)
        # uncommon1 = {ord(letter): '' for letter in text1 if letter not in text2}
        # text1 = text1.translate(uncommon1)
        n1, n2 = len(text1), len(text2)
        grid = [[0 for _ in range(n2+1)] for _ in range(n1+1)] # n2 = cols , n2 = rows
        def helper(idx1, idx2):
            # print(idx1, idx2)
            if idx1 == 0 or idx2 == 0:
                return 0
            if grid[idx1][idx2]:
                return grid[idx1][idx2]
            else:
                if text1[idx1-1] == text2[idx2-1]:
                    grid[idx1][idx2] = 1 + helper(idx1-1, idx2-1)
                else:
                    grid[idx1][idx2] = max(helper(idx1-1, idx2), helper(idx1, idx2-1))
                return grid[idx1][idx2]
        helper(n1, n2)
        if self.verbose:
            print(' ', *text2)
            for row in range(1, len(grid)):
                print(text1[row-1], *grid[row][1:])
        return max([col for row in grid for col in row if isinstance(col, int)])

if __name__ == '__main__':
    text1, text2 = ('abcde', 'ace')
    # text1, text2 = ('abcde', 'afgb')
    # text1, text2 = ('abcde', 'qce')
    # text1, text2 = ('abcde', 'aca')
    # text1, text2 = ('abcde', 'ece')
    # text1, text2 = ('fweoih', 'qwpriufs')
    # text1, text2 = ('fweoihbudaoc', 'qwpriufsdnmsad')
    # text1, text2 = ('fweoihbudaoc', 'qqq')
    # text1, text2 = ('aopsdivopushdvuiwekjbksabviawruvhoisduhwiorvpsioadfvposmdvfhoaweumfoefiwuehgipowaufhposidjfposidjvsdcv', 'aspodihtrjnwepofjpoicvjpoasdhfpoisfuhbpqwneirbneryhiyagfaskdhsafbiosdfinahei')
    # text1, text2 = ('ylqpejqbalahwr', 'yrkzavgdmdgtqpg')

    print(f'text1 = {text1}, text2 = {text2}')
    # print(Solution(True).longestCommonSubsequence(text1, text2))
    print(Solution(True).longestCommonSubsequenceA(text1, text2))