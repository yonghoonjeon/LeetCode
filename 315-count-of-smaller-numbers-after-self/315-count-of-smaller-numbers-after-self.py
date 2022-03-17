class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        def new(val):
            node = TreeNode(val)
            node.size = 0
            node.count = 1
            node.color = True
            return node

        def rotate_left(root):
            right = root.right
            root.color,right.color = right.color,root.color
            root.right,right.left = right.left,root
            right.size += (root.size + root.count)
            return right

        def rotate_right(root):
            left = root.left
            root.color,left.color = left.color,root.color
            root.left,left.right = left.right,root
            root.size -= (left.size + left.count)
            return left

        def flip(root):
            root.left.color = False
            root.right.color = False
            root.color = True
            return root

        def red(node):
            return node != None and node.color

        def insert(root,node):
            # root is empty
            if root == None:
                return node,node.size
            
            if node.val == root.val:
                root.count += 1
                return root,root.size
            
            if node.val < root.val:
                root.size += 1
                root.left,size = insert(root.left,node)
            # node.val > root.val:
            else: 
                root.right,size = insert(root.right,node)
                size += (root.size + root.count)
            
            # right sub-tree is red
            if red(root.right) and not red(root.left):
                root = rotate_left(root)
            # consecutive red edges on left sub-tree
            if red(root.left) and red(root.left.left):
                root = rotate_right(root)
            # both sub-trees are red
            if red(root.left) and red(root.right):
                root = flip(root)

            return root,size


        ret,root = [0 for _ in nums],None
        for i in range(len(nums)-1,-1,-1):
            node = new(nums[i])
            root,size = insert(root, node)
            ret[i] = size
        return ret        