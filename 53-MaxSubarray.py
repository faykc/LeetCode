from functools import reduce

class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(list(filter(lambda x: x>0, nums))) == 0:
            return reduce(lambda elem, result: elem if elem > result else result, nums)
        maxSum = nums[0]
        endIndex = len(nums)
        for startIndex,number in enumerate(nums):
            while endIndex > startIndex and len(list(filter(lambda x: x>=0, nums[startIndex:endIndex]))) != 0:
                if sum(nums[startIndex:endIndex]) > maxSum:
                    maxSum = sum(nums[startIndex:endIndex])
                endIndex -= 1
            endIndex=len(nums)
        return maxSum
