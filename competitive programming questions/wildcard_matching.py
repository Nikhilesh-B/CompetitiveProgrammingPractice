# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_list = []
        curr_node = head
        while curr_node != None:
            node_list.append(curr_node)
            curr_node = curr_node.next

        k = k % len(node_list)
        if k == 0:
            return head
        llist, rlist = node_list[-k:], node_list[:-k]
        llist[-1].next = rlist[0]
        rlist[-1].next =  None
        return llist[0]