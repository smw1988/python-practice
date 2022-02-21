from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        start = ListNode(None, head)
        self._deleteDuplicates(start)
        return start.next

    def _deleteDuplicates(self, head: Optional[ListNode]):
        last = head
        current: Optional[ListNode] = head.next

        while current != None:
            last.next = current
            last = current
            current = self._skipDup(current)

        last.next = None
    
    def _skipDup(self, node: Optional[ListNode]):
        value = node.val
        while node != None and node.val == value:
            node = node.next
        return node

def test(sln, head):
    result = sln.deleteDuplicates(head)
    while result != None:
        print(result.val, end = ' ')
        result = result.next
    print(None)

if __name__ == "__main__":
    sln = Solution()
    test(sln, ListNode(1, ListNode(1, ListNode(2, None))))
    test(sln, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None))))))
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, None))))))))
    test(sln, ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None))))))
    test(sln, None)
    test(sln, ListNode(1, None))
    test(sln, ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(2, None))))))
    test(sln, ListNode(1, ListNode(1, None)))
    test(sln, ListNode(1, ListNode(2, ListNode(2, None))))