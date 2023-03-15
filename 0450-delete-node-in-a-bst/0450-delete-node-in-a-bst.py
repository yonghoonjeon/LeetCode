# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # delete left 
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # delete right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # leaf node
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # full sub-tree
            else:
                # 오른쪽 서브트리에서 min 노드 탐색
                min_node = self.findMinNode(root.right)
                # root에 값 복사
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root
    
    def findMinNode(self, node):
        while node.left:
            node = node.left
        return node
