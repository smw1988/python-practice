class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        last = dummy
        current = head

        while (current != None):
            if current.next == None:
                last.next = current
                break
            else:
                nextIterationStart = current.next.next

                next = current.next
                next.next = current
                last.next = next
                last = current
                current.next = None

                current = nextIterationStart

        return dummy.next