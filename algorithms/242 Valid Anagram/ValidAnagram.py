class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sa=sorted(s)
        ta=sorted(t)
        return sa==ta