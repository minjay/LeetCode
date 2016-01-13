class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = "{0:b}".format(n)
        s = 0
        for i in n:
            s += int(i)
        return s
        