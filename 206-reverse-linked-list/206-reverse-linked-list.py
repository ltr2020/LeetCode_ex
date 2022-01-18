# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # if head = None or head.next = None (reach end of list)
            return head
		# reverse the rest list
        rest = self.reverseList(head.next)
        
		# Put first element at the end
        head.next.next = head # create new pointer from node 2 to node 1
        head.next = None # remove pointer from node 1 to node 2
    
        # Fix the header pointer
        return rest