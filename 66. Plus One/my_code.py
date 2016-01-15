class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        digits = [0]+digits
        digits[n] = digits[n]+1
        i = n
        while digits[i]>9:
            digits[i] = digits[i]%10
            i = i-1
            digits[i] = digits[i]+1
        if digits[0]==0:
            return digits[1:]
        else:
            return digits