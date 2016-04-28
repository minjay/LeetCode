class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        j = 0
        for i in range(l):
            if nums[i]!=0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, l):
            nums[i] = 0