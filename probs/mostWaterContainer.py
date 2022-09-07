# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        ans = 0
        while True:
            # Calculate Area
            startHeight, endHeight = (height[start], height[end])
            lower = min(startHeight, endHeight)
            area = (end - start) * lower
            ans = max(ans, area)

            # Move to next highest
            if height[start] == lower:
                while height[start] <= lower:
                    if start == end:
                        return ans
                    start += 1
            else:
                while height[end] <= lower:
                    if start == end:
                        return ans
                    end -= 1

    def display(self, height):
        highest = sorted(height)[-1]
        array = [['*']*i+[' ']*(highest-i) for i in height]
        for i in range(highest)[::-1]:
            print(*[s[i] for s in array])
        return None

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
    # Solution().display(height)
    pass