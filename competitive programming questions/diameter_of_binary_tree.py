# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: list[TreeNode]) -> int:
        max_diameter = 0
        def max_path_len(node):
            nonlocal max_diameter
            if node == None:
                return -1
            else:            
                l_1, l_2 = max_path_len(node.left), max_path_len(node.right)
                max_diameter = max(l_1+l_2+2,max_diameter)
                return max(l_1+1,l_2+1) 
        
        max_path_len(root)
        return max_diameter



if __name__ == "__main__":
    a,b,c,d,e,f,g,h,i = TreeNode(val=1), TreeNode(val=1), TreeNode(val=1), TreeNode(val=1), TreeNode(val=1), TreeNode(val=1), TreeNode(val=1), TreeNode(val=1), TreeNode(val=1) 
    a.left = b
    b.right = c
    # c.left=d
    # d.left=e
    # e.left=f
    # c.right = g
    # g.right = h
    # h.right = i

    sol = Solution()
    ans = sol.diameterOfBinaryTree(root=a)
    print("The answer is =",ans)