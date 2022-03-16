# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # function to find height of binary tree
    def height(self, root):

        # base condition when binary tree is empty
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base condition 
        if root is None:
            return True

        # get height of left and right sub-trees
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        # balance check
        if (abs(lh - rh) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
        