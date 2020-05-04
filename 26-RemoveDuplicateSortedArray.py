# Problem 26: Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        originalIndex = 1
        for x in nums[originalIndex::]:
            if originalIndex < len(nums) and x==nums[originalIndex-1]:
                nums.remove(x)
            else:
                originalIndex += 1
        return len(nums)