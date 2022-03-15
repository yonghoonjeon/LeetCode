# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None :
            return []
        
        answer = []
        # in-order traversal
        def inorder(node) :
            if node :
                inorder(node.left)
                answer.append(node.val)
                inorder(node.right)
        
        inorder(root)
        
        return answer[k-1]
        
