
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.length(head)
        if (length == n):
            return head.next

        self.removeNth(head, length - n - 1)
        return head

    def length(self, head: ListNode) -> int:
        len = 0
        while (head != None):
            len += 1
            head = head.next
        return len

    def removeNth(self, head: ListNode, n: int):
        prev = head
        current = head.next
        while (n > 0):
            prev = current
            current = current.next
            n -= 1
        prev.next = current.next

if __name__ == "__main__":
    s = Solution()
    