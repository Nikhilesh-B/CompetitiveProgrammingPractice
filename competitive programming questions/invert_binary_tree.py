# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == []:
            return []
        
        def inversion(root):
            if root.left == None and root.right==None:
                return root
            
            else:
                root.left, root.right  = inversion(root.right), inversion(root.left)




if __name__ == "__main__":
    s = Solution()
    
