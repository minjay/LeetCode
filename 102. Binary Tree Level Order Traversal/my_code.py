# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # this is exactly a Breadth-First-Search problem
        # use queue (FIFO)
        if not root:
            return []
        # init a queue that stores leaves at each level
        level = [root]
        trav = []
        # while the tree has been traversed
        while level:
            trav += [[node.val for node in level]]
            tmp = []
            for node in level:
                tmp += [node.left, node.right]
            level = [node for node in tmp if node]
        return trav
        
        