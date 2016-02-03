class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        pt = [[1], [1, 1]]
        pt_sub = [1, 1]
        for i in range(numRows-2):
            pt_sub_new = [1]
            for j in range(len(pt_sub)-1):
                pt_sub_new = pt_sub_new+[pt_sub[j]+pt_sub[j+1]]
            pt_sub_new = pt_sub_new+[1]
            pt_sub = pt_sub_new
            pt = pt+[pt_sub]
        return pt