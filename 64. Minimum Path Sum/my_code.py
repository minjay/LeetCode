class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # it is a dynamic programming problem
        # let f(i, j) denote the minimum of the sum of all numbers along its path to the grid point (i, j)
        # f(i, j) = min{f(i, j-1), f(i-1, j)}+grid(i, j)
        m = len(grid)
        n = len(grid[0])
        # Note: do not use f=[[0]*n]*m
        # to avoid reference sharing between the rows
        f = [[0 for j in range(n)] for i in range(m)]
        f[0][0] = grid[0][0]
        for i in range(1, m):
            f[i][0] = f[i-1][0]+grid[i][0]
        for j in range(1, n):
            f[0][j] = f[0][j-1]+grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = min(f[i-1][j], f[i][j-1])+grid[i][j]
        return f[m-1][n-1]