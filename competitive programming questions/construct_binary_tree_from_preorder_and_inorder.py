#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> list[TreeNode]: 
        if len(preorder) == 0:
            return None 
    
        root_val = preorder[0]
        root_idx = inorder.index(root_val)

        left_inorder = inorder[0:root_idx]
        right_inorder = inorder[root_idx+1:]

        left_most_idx = root_idx-1

        if left_most_idx != -1:
            left_tree_last_val = inorder[left_most_idx]
            preorder_left_idx = preorder.index(left_tree_last_val)
            left_preorder = preorder[1:preorder_left_idx+1]
            right_preorder = preorder[preorder_left_idx+1:]

        else:
            left_preorder = []
            right_preorder = preorder[1:]


        root = TreeNode(val=preorder[0],
                        left=self.buildTree(inorder=left_inorder, preorder=left_preorder),
                        right=self.buildTree(inorder=right_inorder, preorder=right_preorder),)
        
        return root
