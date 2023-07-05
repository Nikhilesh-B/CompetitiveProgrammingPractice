# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_list(self, head):
        curr_node = head
        while curr_node != None:
            print(str(curr_node.val)+"->",end='')
            curr_node = curr_node.next

    def sortList(self, head: list[ListNode]) -> list[ListNode]:
        og_len = self.compute_length(head=head)
        sorted_sub_lists = []
        curr_node = head
        while curr_node != None:
            temp_node = curr_node.next
            curr_node.next = None
            sorted_sub_lists.append(curr_node)
            curr_node = temp_node
        
        while self.compute_length(head=sorted_sub_lists[0])!=og_len:
            new_sub_lists = [] 
            if len(sorted_sub_lists)%2 == 1:
                for i in range(0,len(sorted_sub_lists)-1,2):
                    l1, l2  = sorted_sub_lists[i], sorted_sub_lists[i+1]
                    combined_list = self.combine_lists(l1, l2)
                    new_sub_lists.append(combined_list)
                new_sub_lists.append(sorted_sub_lists[-1])
            else:
                for i in range(0,len(sorted_sub_lists),2):
                    l1, l2  = sorted_sub_lists[i], sorted_sub_lists[i+1]
                    combined_list = self.combine_lists(l1, l2)
                    new_sub_lists.append(combined_list)
            sorted_sub_lists = new_sub_lists
        return sorted_sub_lists[0]

    def combine_lists(self, head1, head2):
        curr_node1 = head1
        curr_node2 = head2
        temp_node = None
        root_node = None
        itr = 0
        while curr_node1 != None or curr_node2 !=None:
            if itr == 0:
                if curr_node1.val<curr_node2.val:
                    root_node = curr_node1
                    curr_node1 = curr_node1.next
                    root_node.next = None
                else:
                    root_node = curr_node2
                    curr_node2 = curr_node2.next
                    root_node.next = None
                temp_node = root_node    
            else:
                if curr_node1 != None and curr_node2!= None: 
                    if curr_node1.val<curr_node2.val:
                        temp_node.next = curr_node1
                        curr_node1 = curr_node1.next
                    else:
                        temp_node.next = curr_node2
                        curr_node2 = curr_node2.next
                    
                elif curr_node1==None:
                    temp_node.next = curr_node2
                    curr_node2 = curr_node2.next
                
                else:
                    temp_node.next = curr_node1
                    curr_node1 = curr_node1.next
                
                temp_node = temp_node.next
                temp_node.next = None

            itr+=1
        return root_node
    
    def compute_length(self, head):
        total = 0
        curr_node = head
        while curr_node != None:
            total+=1
            curr_node = curr_node.next
        
        return total


import random
if __name__ == "__main__":
    sol = Solution()
    high, low = int(1e5),-1*int(1e5)
    length = 50000
    root = ListNode(val=random.randint(low,high))
    curr_node = root
    for _ in range(int(length)):
        new_node = ListNode(val=random.randint(low,high))
        curr_node.next = new_node
        curr_node = new_node
    print("Original list", end='')
    sol.print_list(root)
    print("")
    sorted = sol.sortList(root)
    print("Sorted =", end='')
    sol.print_list(sorted)