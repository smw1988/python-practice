
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0: return head
        if head == None: return head

        (length, last) = self.length(head)
        k = k % length
        if k == 0: return head
        if length == 1: return head

        steps = length - 1 - k
        end = head
        while steps > 0:
            end = end.next
            steps -= 1

        start = end.next
        end.next = None
        last.next = head
        return start

    def length(self, head: ListNode):
        if head == None: return 0
        n = 1
        while head.next != None:
            head = head.next
            n += 1
        return (n, head)

def test(sln, head, k):
    result = sln.rotateRight(head, k)
    while result != None:
        print(result.val, end = ' ')
        result = result.next
    print(None)

if __name__ == "__main__":
    sln = Solution()
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 0)
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1)
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 4)
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5)
    test(sln, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 6)

    test(sln, ListNode(1, ListNode(2, ListNode(3))), 0)
    test(sln, ListNode(1, ListNode(2, ListNode(3))), 1)
    test(sln, ListNode(1, ListNode(2, ListNode(3))), 2)
    test(sln, ListNode(1, ListNode(2, ListNode(3))), 3)

    test(sln, ListNode(1, ListNode(2)), 0)
    test(sln, ListNode(1, ListNode(2)), 1)
    test(sln, ListNode(1, ListNode(2)), 2)

    test(sln, ListNode(1), 0)
    test(sln, ListNode(1), 1)

    test(sln, None, 0)
    test(sln, None, 1)
