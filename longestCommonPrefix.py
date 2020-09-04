"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        # get length of array
        n = len(strs)
        if n == 0:
            return ""
        result = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        limit = min(len(first), len(last))
        for i in range(limit):
            if first[i] == last[i]:
                result += first[i]
            else:
                break
        return result
