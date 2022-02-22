from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        start = ListNode(None, head)

        # middle is the previous node of the first node >= x, if any;
        # or last node if none exists
        middle = self._findMiddle(start, x)
        current = middle.next
        prev = middle

        while current != None:
            next = current.next
            if current.val < x:
                # unlink
                nodeToMove = current
                prev.next = next
                current = next

                # insert
                nodeToMove.next = middle.next
                middle.next = nodeToMove
                middle = nodeToMove

            else:
                prev = current
                current = next

        return start.next

    def _findMiddle(self, head: Optional[ListNode], x: int):
        current = head
        while current.next != None and current.next.val < x:
            current = current.next
        return current

def buildLinkedListFromArray(values: List[int]):
    head = None
    for i in range(len(values) - 1, -1, -1):
        head = ListNode(values[i], head)
    return head

def linkedListToArray(head: ListNode):
    array = []
    while head != None:
        array.append(head.val)
        head = head.next
    return array

def test(sln, values, x):
    result = sln.partition(buildLinkedListFromArray(values), x)
    print(linkedListToArray(result))

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1,4,3,2,5,2], 3)
    test(sln, [2,1], 2)
    test(sln, [], 1)
    test(sln, [3,4,5], 3)
    test(sln, [1,2,3], 4)