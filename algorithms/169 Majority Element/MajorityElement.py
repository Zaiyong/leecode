class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        max_=max(dict.itervalues())
        for i,j in dict.iteritems():
            if j==max_: return i