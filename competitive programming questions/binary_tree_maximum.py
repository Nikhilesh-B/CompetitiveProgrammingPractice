#
# class Node(): /n def __init__(self): /n self.left = child1, self.right =child2, self.val=val
import math

class Solution():
    def __init__(self):
        self.max_val = -math.inf

    def binary_tree_maximum_sum(self, root):
        self.recursive_root_value(root)
        return self.max_val

    def recursive_root_value(self, root):
        if not root:
            return 0
        else:
            mx_left_sum = self.recursive_root_value(root.left)
            mx_right_sum = self.recursive_root_value(root.right)
            self.max_val = max(self.max_val, mx_left_sum, mx_right_sum)

            return max(root.val+mx_left_sum, root.val+mx_right_sum)

if __name__ == "__main__":
    pass