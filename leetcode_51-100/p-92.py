from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newListLen = right - left
        if newListLen == 0:
            return head

        # dummy header
        head = ListNode(0, head)
        prev: ListNode = head; current: ListNode = head.next

        while left > 1:
            prev = current
            current = current.next
            left -= 1

        reverseHead: ListNode = prev
        newListLast: ListNode = current

        while newListLen >= 0:
            next = current.next
            current.next = prev
            prev = current
            current = next
            newListLen -= 1

        newListStart: ListNode = prev
        reverseTail: ListNode = current

        reverseHead.next = newListStart
        newListLast.next = reverseTail

        return head.next

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

def test(sln, values, left, right):
    result = sln.reverseBetween(buildLinkedListFromArray(values), left, right)
    print(linkedListToArray(result))

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1,2,3,4,5], 2, 4)
    test(sln, [5], 1, 1)
    test(sln, [1,2,3,4,5], 1, 1)
    test(sln, [1,2,3,4,5], 5, 5)
    test(sln, [1,2,3,4,5], 1, 2)
    test(sln, [1,2,3,4,5], 4, 5)
    test(sln, [1,2,3,4,5], 1, 5)
    test(sln, [1,2], 1, 2)