# note that coversion between int and str is time-consuming
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            s = 0
            while num>0:
                s += num%10
                num = num/10
            num = s
        return num