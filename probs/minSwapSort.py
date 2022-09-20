# Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

from typing import List
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        tmp = nums.copy()
        sortedNums = sorted(nums)
        if self.verbose:
            print(nums, '->', sortedNums)
        sortedNumsMap = {num: idx for idx, num in enumerate(sortedNums)}
        count = 0
        swapped = []
        for idx in range(len(nums)):
            if nums[idx] != sortedNums[idx] and nums[idx] not in swapped:
                swapped.append(nums[idx])
                curr = idx
                while True:
                    if tmp[idx] == sortedNums[idx]:
                        break
                    else:
                        curr = sortedNumsMap[nums[curr]]
                        swapped.append(nums[curr])
                        Solution.swap(tmp, idx, curr)
                        count += 1
                        if self.verbose:
                            print(f'{tmp} : {tmp[curr]} -> {tmp[idx]}')
        return count
        
    def minimumSwapsA(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        sortedNumsMap = {num: idx for idx, num in enumerate(sortedNums)}
        count = 0
        swapped = []
        for idx in range(len(nums)):
            if nums[idx] != sortedNums[idx] and nums[idx] not in swapped:
                swapped.append(nums[idx])
                curr = sortedNumsMap[nums[idx]]
                while idx != curr:
                    swapped.append(nums[curr])
                    curr = sortedNumsMap[nums[curr]]
                    count += 1
        return count
    
    def __init__(self, verbose=False):
        self.verbose = verbose

    @staticmethod
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    nums = [2, 8, 5, 4]
    nums = [10, 19, 6, 3, 5]
    nums = [10, 19, 6, 3, 5, 1]
    nums = [34, 15, 24, 95, 59, 99, 40, 11, 54, 23, 79, 5]
    print(Solution(verbose=True).minimumSwaps(nums), '=', Solution().minimumSwapsA(nums))