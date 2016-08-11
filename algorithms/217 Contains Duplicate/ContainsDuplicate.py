class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l_orig=len(nums)
        l_cur=len(set(nums))
        if l_orig>l_cur: return True
        return False