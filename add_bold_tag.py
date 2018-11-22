
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Add bold tag
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:

Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

"""

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if not s:
            return ""
        n = len(s)
        intervals = [False] * n
        for word in dict:
            start = s.find(word)
            l = len(word)
            while start != -1:
                for i in range(start, start+l):
                    intervals[i] =True
                start = s.find(word,start+1)

        i = 0
        o = ""
        while i < n:
            if intervals[i]:
                o += "<b>"
                while i < n and intervals[i]:
                    o += s[i]
                    i += 1
                o += "</b>"
            else:
                o += s[i]
                i += 1
        return o
