class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        last = head

        while (l1 != None and l2 != None):
            if (l1.val < l2.val):
                last.next = l1
                last = l1
                l1 = l1.next
            else:
                last.next = l2
                last = l2
                l2 = l2.next
        
        if (l1 != None):
            last.next = l1
        if (l2 != None):
            last.next = l2

        return head.next