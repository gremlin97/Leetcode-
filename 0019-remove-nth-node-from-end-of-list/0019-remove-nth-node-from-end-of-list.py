# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode()
        dummy.next = head
        
        slow = fast = dummy
        
        while fast.next and n>0:
            print(fast.val)
            fast = fast.next
            n-=1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        print(slow.val, fast.val)
        
        slow.next = slow.next.next
        return dummy.next
        