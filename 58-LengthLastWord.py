# Problem 58: Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        updatedList = list(filter(lambda x: x!='', re.split('\s+', s)))
        return len(updatedList[len(updatedList)-1]) if len(updatedList)!=0 else 0