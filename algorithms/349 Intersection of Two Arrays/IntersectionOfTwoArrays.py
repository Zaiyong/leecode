class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        inter=[val for val in nums1 if val in nums2]
        for i in inter:
            if i not in result:
                result.append(i)
        return result