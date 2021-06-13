class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if (k == 1):
            return head

        dummy = ListNode(head)
        workingLast = dummy
        newIterStart = head
        while (newIterStart != None):
            (count, newIterEnd, nextIterStart) = self.reverse(newIterStart, k)

            if (count < k):
                self.reverse(newIterEnd, k)
                workingLast.next = newIterStart
                break

            workingLast.next = newIterEnd
            workingLast = newIterStart
            newIterStart = nextIterStart

        return dummy.next

    def reverse(self, start: ListNode, k: int):
        prev = start
        current = start.next
        count = 1

        while (current != None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        start.next = None
        return (count, prev, current)
        