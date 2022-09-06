# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # check if order is possible:
        if start.replace('_', '') == target.replace('_', ''):
            return self.helper(start, target)
        else:
            return False

    def helper(self, start: str, target: str) -> bool:
        d = {
            'start': {
                'L': [idx for idx, val in enumerate(start) if val == 'L'],
                'R': [idx for idx, val in enumerate(start) if val == 'R']
            },
            'target': {
                'L': [idx for idx, val in enumerate(target) if val == 'L'],
                'R': [idx for idx, val in enumerate(target) if val == 'R']
            },
        }
        # L
        n = len(d['start']['L'])
        for i in range(n):
            if d['start']['L'][i] < d['target']['L'][i]:
                return False

        # R
        n = len(d['start']['R'])
        for i in range(n):
            if d['start']['R'][i] > d['target']['R'][i]:
                return False

        return True

    def helper1(self, start: str, target: str) -> bool:
        n = len(start)
        p1 = p2 = 0
        while p1 < n and p2 < n:
            compare = [start[p1], target[p2]]
            if '_' in compare:
                if start[p1] == '_':
                    p1 += 1
                if start[p2] == '_':
                    p2 += 1
                continue
            else:
                pass
        return n

if __name__ == '__main__':
    start = '_L__R__R_'; target = 'L______RR'
    print(f'{start} -> {target}\n{Solution().canChange(start, target)}')