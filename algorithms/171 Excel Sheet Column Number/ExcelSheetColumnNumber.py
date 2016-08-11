import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column_num=0
        all_letters=string.uppercase
        reverse_s=s[::-1]
        for i in range( len(reverse_s)):
            column_num+=(all_letters.find(reverse_s[i])+1)*(26**i)
        return column_num