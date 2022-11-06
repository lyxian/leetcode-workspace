# Alice and Bob are opponents in an archery competition. The competition has set the following rules:
# 
# Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
# The points are then calculated as follows:
# The target has integer scoring sections ranging from 0 to 11 inclusive.
# For each section of the target with score k (in between 0 to 11), say Alice and Bob have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.
# However, if ak == bk == 0, then nobody takes k points.
# For example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.
# 
# You are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.
# 
# Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.
# 
# If there are multiple ways for Bob to earn the maximum total points, return any one of them.

from typing import List
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        numSections = 11
        def helper(idx, arrowsLeft, score, bobArrows):
            if arrowsLeft < 0:
                return -1, bobArrows
            if idx == 0 or arrowsLeft == 0:
                bobArrows[0] = arrowsLeft
                return score, bobArrows
            if aliceArrows[idx]:
                print(f'{idx} challenged, left {arrowsLeft} arrows')
                tmp = bobArrows.copy()
                tmp[idx] += aliceArrows[idx] + 1
                return max(helper(idx-1, arrowsLeft-aliceArrows[idx]-1, score+idx, tmp), \
                    helper(idx-1, arrowsLeft, score, bobArrows))
            else:
                print(f'{idx} free, left {arrowsLeft} arrows')
                bobArrows[idx] += 1
                return helper(idx-1, arrowsLeft-1, score+idx, bobArrows)
        return helper(numSections, numArrows, 0, [0] * 12)[1]

if __name__ == '__main__':
    numArrows = 3
    aliceArrows = [0,0,0,0,0,0,0,0,0,1,2,0]
    numArrows = 89
    aliceArrows = [3,2,28,1,7,1,16,7,3,13,3,5] # [21,3,0,2,8,2,17,8,4,14,4,6]
    print(Solution().maximumBobPoints(numArrows, aliceArrows))