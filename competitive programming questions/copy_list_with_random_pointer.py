# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def print_list(self, head):
        curr_node = head
        while curr_node != None:
            print(curr_node.val, end='')
            print('->',end='')
            curr_node=curr_node.next
        print('\n')

    def copyRandomList(self, head):
        curr_new_node = None
        curr_old_head = head
        prev_new_node = None
        while curr_old_head != None:
            if curr_new_node == None:
                curr_new_node = Node(x=curr_old_head.val)
                new_root_node = curr_new_node
            else:
                curr_new_node = Node(x=curr_old_head.val)
            if prev_new_node != None:
                prev_new_node.next = curr_new_node
            prev_new_node = curr_new_node
            curr_old_head =  curr_old_head.next
    
        print(new_root_node, head)
        self.print_list(new_root_node)
        self.print_list(head)

        curr_old_head = head
        temp_new_head = new_root_node
        while curr_old_head != None: 
            if curr_old_head.random != None:
                length = self.return_length_og_list(head, curr_old_head.random)
                print(length)
                temp_temp_new_head = new_root_node
                for _ in range(length):
                    temp_temp_new_head = temp_temp_new_head.next
                temp_new_head.random = temp_temp_new_head
                    
            curr_old_head =  curr_old_head.next
            temp_new_head =  temp_new_head.next

        return new_root_node

    def return_length_og_list(self, head, target):
        length = 0 
        curr_node = head
        while curr_node != target:
            curr_node = curr_node.next
            length += 1
        return length


        
if __name__ == "__main__":
    sol = Solution()
    a, b, c = Node(x=1), Node(x=2), Node(x=3)
    a.next = b 
    a.random = c
    b.next = c
    sol.copyRandomList(a)