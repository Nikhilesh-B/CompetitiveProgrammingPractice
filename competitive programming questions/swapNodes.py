class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: list[ListNode]) -> list[ListNode]:
        if head == None:
            return None

        if head != None and head.next==None:
            return head


        counter = 0
        currNode = head
        return_node = None
        tie_node = None
        while currNode != None and currNode.next!= None:
            print(currNode.val, currNode.next.val, counter)
            if counter == 0:
                temp_next = currNode.next
                currNode.next = currNode.next.next
                temp_next.next = currNode
                return_node = temp_next

            else:
                if counter%2==1:
                    tie_node = currNode
                    currNode = currNode.next
                
                else:
                    temp_next = currNode.next
                    currNode.next = currNode.next.next
                    temp_next.next = currNode
                    tie_node.next = temp_next

            counter+=1
        
        return return_node