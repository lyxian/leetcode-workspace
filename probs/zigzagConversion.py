# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

class Solution:
    verbose = True
    # verbose = False

    def __init__(self, correct=False):
        self.correct = correct

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::numRows] + s[1::numRows]
        else:
            if self.correct:
                grid = self.display(s, numRows)
                return ''.join([''.join([_ for _ in i]) for i in grid]).replace(' ', '')
            else:
                skip = 2 * numRows - 2
                makeUp = (len(s) - 1) % skip
                if makeUp:
                    s += ' ' * makeUp
                ans = s[::skip]
                for i in range(1, numRows-1):
                    for j in range(0, len(s), skip):
                        if j - i < 0:
                            if j + i == len(s):
                                break
                            ans += s[j+i]
                        elif j + i >= len(s):
                            ans += s[j-i]
                        else:
                            ans += s[j-i]
                            ans += s[j+i]
                return f'{ans}{s[numRows-1::skip]}'.replace(' ', '')
    
    def display(self, s: str, numRows: int, verbose=False) -> str:
        numCols = (len(s) // (2 * numRows - 2) + 1) * (numRows - 1)
        grid = [[' ' for _ in range(numCols)] for _ in range(numRows)]
        x = y = 0; goingDown = True
        for character in s:
            grid[x][y] = character
            if x == 0:
                goingDown = True
            elif x == numRows - 1:
                goingDown = False
            if goingDown:
                x += 1
            else:
                y += 1; x -= 1
        if verbose and self.verbose:
            print(f'{numRows} X {numCols} Grid: ')
            for i in grid:
                print(*[j for j in i], sep=' ')

        return grid

if __name__ == '__main__':
    s = 'PAYPALISHIRING'; numRows = 4
    # s = 'oxjpkcpdekyazevyzxudsirvddoxmptaodryfhdltcmuijsigolaxevcimbwduwrzqrhxvssxgmhpgpxvdyujvwrhzpktmdvcvcbquvpbhwsposktsecncwxbljxznsdiugaqbprknmabekwwrzltxixiuwihonrkutaviuixgibkuxinythvcgewcofsbycxrctbydyelzqhzyvxsetwkzuonbgqziosmjvnmtrzvkiuidrcjkavlwjaxrrybhsqsndghwhegpyrvrvgcwcpsnqsfjqgqjykwbqfyzjeojxlbtsfpwujjkbqtuzldxxbznjxmuddedqhwioneiwqvygqufezdbacrlbfggkmjbvfjjsqtrgormhlulkxombfyengkxuwypdkyyarpiiiwptqcdnsrqypunxfkrdlggvggxaxhifdzyuddjvvcvkwikdvbggkpbqvyqvfaakzzgecsazuxmqgwwbxchhtkarkqmrrmbsnixsczrwwdoebkfzpoikyibkbpbuedmrnllpkfnjkbnmovnfjxpkitwjiydmdrgqdthpywyjzmvnhksshkepdbylbdaexiwabfrabqlaegqnskhzumpzpplqvnwsvsuwxlyabjchruujhclbqcbhtozobviypcwmoxoriqbanvluzyxpaawwovkrsvrhxotnnjhvcivpfjjfjgwkhtgxqsrjpiqnymclvlhxveobpxgzgclnxtmqndzdmrsmduybifadlpebomaurljoewerzfwnxoacjydrfeuqvbtjnteegnvmjbgljcygraicamvfspynsrwgnamvqjiblomuqlcjnkloygvsytfqneycglxwwfyhtkdmxhvlujbspwlnqsefwchdpezmmzvfkbtjirwcaxxpukfmcltznaefgdtsdqaprvacmxemubeoljcquvpjxvqeajwfcyutuvvgscv'; numRows = 918
    Solution().display(s, numRows, True)
    print(f'===SOLUTION===\n{Solution(correct=True).convert(s, numRows)}')
    print(f'===ATTEMPT===\n{Solution().convert(s, numRows)}')
    