class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        digit_list=map(int,str(num))
        digit_list2=map(int,str(sum(digit_list)))
        digit_list3=map(int,str(sum(digit_list2)))
        digit_list4=map(int,str(sum(digit_list3)))
        return digit_list4[0]