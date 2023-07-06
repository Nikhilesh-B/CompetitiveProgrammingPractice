class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __print__(self):
        print(self.val)

class Solution:
    def compute_length(self, head):
        length = 0
        curr_node = head
        while curr_node != None:
            length += 1
            curr_node = curr_node.next 
        return length
    

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> list[ListNode]:
        lenA = self.compute_length(head=headA)
        lenB = self.compute_length(head=headB)
        curr_node_a = headA
        curr_node_b = headB
        if lenA > lenB:
            dif = lenA-lenB
            for _ in range(dif):
                curr_node_a = curr_node_a.next
            
            while curr_node_a != curr_node_b and (curr_node_a!= None and curr_node_b!= None):
                curr_node_a = curr_node_a.next
                curr_node_b = curr_node_b.next

          
        else:
            dif = lenB-lenA
            for _ in range(dif):
                curr_node_b = curr_node_b.next
            
            while curr_node_a != curr_node_b and (curr_node_a!= None and curr_node_b!= None):
                curr_node_a = curr_node_a.next
                curr_node_b = curr_node_b.next
            
        if curr_node_a==None and curr_node_b==None:
            return None
        
        else:
            return curr_node_a