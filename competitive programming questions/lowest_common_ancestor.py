# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left =  None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        
        p_path = self.perform_search(root=root, target=p)
        q_path = self.perform_search(root=root, target=q)

        print(p_path)
        print(q_path)
        common_prefix_string = self.common_prefix(p_path,q_path)
        print(common_prefix_string)

        return_node = self.traversal(root=root,path=common_prefix_string)
        return return_node

    def traversal(self, root, path):
        curr_node = root
        for step in path:
            if step == "L":
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return curr_node

    def common_prefix(self, p1, p2):
        prefix_str = ""
        shorter_len = min(len(p1),len(p2))
        for i in range(shorter_len):
            if p1[i] == p2[i]:
                prefix_str+=p1[i]
            else:
                return prefix_str
        
        if len(p1)>len(p2): return p2 
        else: return p1

    


    def perform_search(self, root: TreeNode, target: TreeNode) -> str:
        traversal = ""
        queue = [root]
        current_traversals = [traversal]
        while queue:
            node = queue.pop(0)
            current_traversal = current_traversals.pop(0)
            if node.val == target.val:
                return current_traversal

            if node.right != None:
                new_traversal = current_traversal + "R"
                queue.append(node.right)
                current_traversals.append(new_traversal)

            if node.left != None:
                new_traversal = current_traversal + "L"
                queue.append(node.left)
                current_traversals.append(new_traversal)

        return None




if __name__ == "__main__":
    sol = Solution()
    r, s = TreeNode(x=-9), TreeNode(x=2)
    p, q = TreeNode(x=10), TreeNode(x=11)
    root = TreeNode(x=1)
    root.left = p
    root.right = q
    p.left = r
    p.right = s 
    print(sol.lowestCommonAncestor(root,r,s).val)
