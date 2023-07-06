# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __print__(self):
        print(self.val)

class Solution:
    def reverseKGroup(self, head: list[ListNode], k: int) -> list[ListNode]:
        length = self.compute_length(head)
        counter = length
        curr_node = head
        tie_node = None
        return_node = None
        while counter >= k:
            new_start, new_end, next_node = self.reverse_up_to_k(curr_node, k)
            if tie_node != None:
                tie_node.next = new_start
            else:
                return_node = new_start
            tie_node = new_end
            curr_node = next_node
            counter -= k
        
        tie_node.next = curr_node
        return return_node

    def compute_length(self, head):
        length = 0
        curr_node = head
        while curr_node != None:
            length += 1
            curr_node = curr_node.next 
        return length
    
    def reverse_up_to_k(self, head, k):
        counter = 0
        new_end = head
        curr_node = head
        prev_node = None
        while counter<k:
            temp_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_node
            counter += 1
        
        new_start = prev_node
        next_node = temp_node
        return new_start, new_end, next_node
    
    def print_list(self, head):
        curr_node = head
        while curr_node != None:
            print(str(curr_node.val)+"->",end='')
            curr_node = curr_node.next
        print('\n')

if __name__ == "__main__":
    sol = Solution()
    a,b,c,d,e = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    # d.next = e
    # print("Existing list")
    # sol.print_list(a)
    new_list = sol.reverseKGroup(head=a, k=4)
    print("Sorted by k groups list")
    sol.print_list(new_list)
