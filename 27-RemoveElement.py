# Problem 27: Remove Element
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        x=0
        while (x<len(nums)):
            if nums[x]==val:
                nums.remove(nums[x])
            else:
                x += 1
        return len(nums)