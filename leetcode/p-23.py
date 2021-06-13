from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self, head: ListNode):
        self.head = head

class Heap:
    def __init__(self, lists: List[LinkList]):
        self.lists = lists
        self.size = len(lists)
        self.makeHeap()

    def makeHeap(self):
        if (self.size > 1):
            for i in range(self.size // 2 - 1, -1, -1):
                self.heapifySubTree(i)

    def heapifySubTree(self, i: int):
        left = self.left(i)
        right = left + 1
        if (left < self.size):
            if (right >= self.size or self.prior(left, right)):
                if (self.prior(left, i)):
                    self.swap(i, left)
                    self.heapifySubTree(left)
            elif (self.prior(right, i)):
                self.swap(i, right)
                self.heapifySubTree(right)
    
    def pop(self):
        self.size -= 1
        if (self.size > 0):
            self.lists[0] = self.lists[self.size]
            self.heapifySubTree(0)

    def top(self):
        return self.lists[0]

    def count(self):
        return self.size

    def left(self, i: int):
        return i + i + 1

    def right(self, i: int):
        return i + i + 2

    def prior(self, i: int, j: int) -> bool:
        return self.lists[i].head.val < self.lists[j].head.val

    def swap(self, i: int, j: int):
        t = self.lists[i]
        self.lists[i] = self.lists[j]
        self.lists[j] = t

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists2 = [ LinkList(l) for l in lists if l != None ]

        if (len(lists2) == 0):
            return None

        result = []
        heap = Heap(lists2)
        while (heap.count() > 0):
            topList = heap.top()
            result.append(topList.head.val)

            topList.head = topList.head.next
            if (topList.head == None):
                heap.pop()
            else:
                heap.heapifySubTree(0)

        return result

if __name__ == "__main__":
    s = Solution()

    lists = [
        ListNode(1),
        ListNode(0)
    ]

    result = s.mergeKLists(lists)
    print(result)