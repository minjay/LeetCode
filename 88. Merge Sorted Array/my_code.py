class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # while nums2 is non-empty
        while n>0:
            # if the last number of nums1 is larger than the last number of nums2
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            # else
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            # if nums1 becomes empty, no longer need to compare, move the whole nums2 to nums1
            if m==0:
                nums1[:n] = nums2[:n]
                n = 0
            