# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr_node = head
        prev_node = None

        while curr_node != None:
            if prev_node != None:
                prev_node.next = head
            if curr_node.next == head:
                return True
            prev_node = curr_node
            curr_node = curr_node.next

        return False



if __name__ == "__main__":
    a, b, c = ListNode(x=1), ListNode(x=2), ListNode(x=3)
    a.next = b
    b.next = c
    #c.next = b
    
    sol = Solution()

    print(sol.hasCycle(a))

