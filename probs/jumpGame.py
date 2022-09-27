# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for idx in range(last)[::-1]:
            print(f'{idx} + {nums[idx]} >= {last}')
            if idx + nums[idx] >= last:
                last = idx
        return last == 0

    def canJumpA(self, nums: List[int]) -> bool:
        # Go from back
        n = len(nums)
        if n == 1:
            return True
        validIndex = [n-1]
        while validIndex:
            curr = validIndex.pop()
            print(f'====\n{curr} == {list(enumerate(nums[:curr][::-1], start=1))}\n----')
            for distance, jump in enumerate(nums[:curr][::-1], start=1):
                print(f'{distance} -> {jump}')
                if distance <= jump:
                    if curr - distance == 0:
                        return True
                    else:
                        validIndex.append(curr - distance)
            print(f'Valid Index = {validIndex}')
        return False

    def canJumpB(self, nums: List[int]) -> bool:
        n = len(nums)
        self.canReach = False
        def helper(idx):
            if self.canReach:
                return
            if idx >= n or not nums[idx]:
                return
            # print(f'Moving {nums[idx]} from index={idx} :')
            moves = nums[idx]
            if moves == 1:
                if idx + 2 == n:
                    self.canReach = True
                    print(f'Last is {nums[idx]} jumps from index={idx}')
                    return
                helper(idx+1)
            else:
                for num in range(nums[idx]):
                    if idx+nums[idx]-num == n -1:
                        self.canReach = True
                        print(f'Last is {nums[idx]} jumps from index={idx}')
                        return
                    helper(idx+nums[idx]-num)
        helper(0)
        return self.canReach

if __name__ == '__main__':
    nums = [0,2,3]
    nums = [2,3,1,1,4]
    # nums = [1,3,1,1,4]
    # nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    # nums = [2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1]
    # nums = [2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4]
    # nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(nums)
    print(Solution().canJump(nums))