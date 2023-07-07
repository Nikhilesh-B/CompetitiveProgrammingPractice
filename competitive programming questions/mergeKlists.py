# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_nums(self, freq, values, head):
        curr_node = head
        while curr_node!=None:
            if curr_node.val not in freq:
                freq[curr_node.val] = 1
                values.add(curr_node.val)
            else:
                freq[curr_node.val] += 1
            curr_node = curr_node.next


    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists: 
            return None 
        
        else:
            freqs = {}
            saved_val = set()
            for lst in lists: 
                self.add_nums(freqs, saved_val, lst)
            nums = sorted(list(saved_val))
        
            counter = 0
            prev_node = None
            for num in nums:
                for _ in freqs[num]:
                    curr_node = ListNode(val=num)
                    if counter == 0:
                        starting_node = curr_node
                        counter = 1

                    if prev_node != None:
                        prev_node.next = curr_node

                    prev_node = curr_node
            
            return starting_node



            