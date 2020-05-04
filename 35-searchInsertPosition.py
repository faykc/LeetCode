# Problem 35: Search Insert Position
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for index,number in enumerate(nums):
            if (target == number):
                return index
            elif (target < number):
                return index
            elif (target > number and index + 1 == len(nums)):
                return index+1
        return 0