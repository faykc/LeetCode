# Problem 14 - Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def shortestWord(self, strs: list) -> int:
        smallest = len(strs[0])
        for x in strs:
            if len(x) < smallest:
                smallest = len(x)
        return smallest

    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ""
        endIndex = self.shortestWord(strs)
        while (endIndex > 0):
            result = list(filter(lambda y: y[0:endIndex]==strs[0][0:endIndex], strs))
            if len(result) != len(strs):
                endIndex -= 1
            else:
                break
        return "" if (endIndex==0) else strs[0][0:endIndex]