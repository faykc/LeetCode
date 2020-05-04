# Problem 38: Count and Say
# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            value = Solution.countAndSay(self, n-1)
            occurrences = 0
            index = 0
            returnVal = ""
            character = value[index]
            while (index < len(value)):
                if (value[index] == character):
                    occurrences += 1
                else:
                    returnVal += "{}{}".format(occurrences,character)
                    if (index < len(value)):
                        occurrences = 1
                        character = value[index]
                index += 1
                if (index == len(value)):
                    returnVal += "{}{}".format(occurrences,character)
            return returnVal  