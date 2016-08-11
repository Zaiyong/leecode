class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        N0=0
        for num in nums:
            if  num !=0:
                nums[N0]=num
                N0+=1
        for i in range(N0,length):
            nums[i]=0