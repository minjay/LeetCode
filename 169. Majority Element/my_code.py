class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use dictionary to achieve it
        dict = {}
        l = len(nums)
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        thres = l/2
        for i in dict:
            if dict[i]>thres:
                return(i)