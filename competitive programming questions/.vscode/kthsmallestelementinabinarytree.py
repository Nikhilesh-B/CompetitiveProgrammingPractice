# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     zero_index_k = k-1 
    #     ordered_vals = []

    #     def insert_vals(node: TreeNode, parent_idx: int, left: bool, left_and_right:bool, ordered_vals):
    #         if node == None:
    #             return
    #         elif parent_idx == None:
    #             ordered_vals.append(node.val)
    #             insert_vals(node.left, 0, True, ordered_vals)
    #             insert_vals(node.right, 0, False, ordered_vals)
    #         else:
    #             if left:
    #                 print(ordered_vals[0:parent_idx], ordered_vals[parent_idx], ordered_vals[parent_idx:], node.val)
    #                 ordered_vals = ordered_vals[0:parent_idx]+[node.val]+ordered_vals[parent_idx:]
    #                 print(ordered_vals)
    #                 if node.left != None and node.right!= None:
    #                     insert_vals(node.left, parent_idx-1, True, left_and_right= True, ordered_vals)
    #                     insert_vals(node.right, parent_idx-1, False, left_and_right=True, ordered_vals)
                    
    #             else:
    #                 ordered_vals = ordered_vals[0:parent_idx+1]+[node.val]+ordered_vals[parent_idx+1:]
    #                 print(ordered_vals)
    #                 insert_vals(node.left, parent_idx+1, True, ordered_vals)
    #                 insert_vals(node.right, parent_idx+1, False, ordered_vals)
        
    #     insert_vals(root, None, None,ordered_vals)
    #     print(ordered_vals)
    #     return ordered_vals[zero_index_k]
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        zero_index_k = k-1 
        vals = []

        def traverse(node:TreeNode):
            if node:
                traverse(node.left)
                vals.append(node.val)
                traverse(node.right)

        
        traverse(root)    
        vals.sort()
        return vals[zero_index_k]



if __name__ == "__main__":
    l = TreeNode(val=4)
    r = TreeNode(val=6)
    t = TreeNode(val=5, left=l, right=r)

    s = Solution()
    ans = s.kthSmallest(t, k=2)
    print("The answer is=",ans)

