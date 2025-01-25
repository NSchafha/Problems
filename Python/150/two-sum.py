from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in numMap:
                return [numMap[diff], i]
            numMap[num] = i
        return False