# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.

from typing import List
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max([len(word) for word in words])
        array = []
        for i in range(n):
            array += [''.join([word[i] if i < len(word) else ' ' for word in words]).rstrip()]
        return array

if __name__ == '__main__':
    s = 'HOW ARE YOU'
    s = 'TO BE OR NOT TO BE'
    print(Solution().printVertically(s))