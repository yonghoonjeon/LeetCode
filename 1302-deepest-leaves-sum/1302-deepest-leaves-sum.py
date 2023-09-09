# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:

            # Compute the depth of each subtree
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # deepest leaf node
        res = 0
        # tree level
        tree_level = self.maxDepth(root)
        # curLevel 
        curLevel = 1
        if root == None:
            return
        q = [(root, curLevel)]
        while q:
            curNode, curLevel = q.pop(0)
            if tree_level == curLevel:
                res += curNode.val
            for i in range(2):
                if i == 0 and curNode.left:
                    q.append((curNode.left, curLevel+1))
                elif i == 1 and curNode.right:
                    q.append((curNode.right, curLevel+1))
        return res
        
        