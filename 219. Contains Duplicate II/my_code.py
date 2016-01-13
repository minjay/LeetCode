class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # O(n) time complexity
        # use dictionary
        n = len(nums)
        dict = {}
        for i in range(n):
            ele = nums[i]
            if ele in dict:
                diff = i-dict[ele]
                if diff<=k:
                    return True
            dict[ele] = i
        return False
            