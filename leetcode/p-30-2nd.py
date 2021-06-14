# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]

# s = "wordgoodgoodgoodbestword" words = ["word","good","best","good"]
# Output: [8]

from typing import List
from collections import deque
import re

class ArrayQueue:
    def __init__(self, length: int) -> None:
        self.array = [None] * (length + 1)
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, e: int) -> bool:
        if (self.full()):
            return False
        else:
            self.doEnqueue(e)

    def doEnqueue(self, e: int):
        newTail = 0 if (self.tail + 1 == len(self.array)) else self.tail + 1
        self.tail = newTail
        self.array[self.tail] = e
        self.count += 1

    def dequeue(self) -> int:
        if (self.head != self.tail):
            self.head = 0 if (self.head + 1 == len(self.array)) else self.head + 1
            self.count -= 1
            return self.array[self.head]
        else:
            return None

    def peak(self) -> int:
        if (self.head != self.tail):
            newHead = 0 if (self.head + 1 == len(self.array)) else self.head + 1
            return self.array[newHead]
        else:
            return None

    def enqueueAndDequeue(self, e: int) -> int:
        if (self.full()):
            self.tail = 0 if (self.tail + 1 == len(self.array)) else self.tail + 1
            self.head = 0 if (self.head + 1 == len(self.array)) else self.head + 1
            old = self.array[self.head]
            self.array[self.tail] = e
            return old
        else:
            self.doEnqueue(e)
            return None

    def full(self) -> bool:
        return (self.tail + 1 == self.head) or (self.head == 0 and self.tail + 1 == len(self.array))

    def empty(self) -> bool:
        return self.head == self.tail

    def clear(self):
        self.head = 0
        self.tail = 0
        self.count = 0

class Solution:
    def removeDup(self, words: List[str]):
        m = {}
        for w in words:
            if (w in m):
                m[w] = m[w] + 1
            else:
                m[w] = 1
        return m

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        fullWordCount = len(words)
        wordLen = len(words[0])
        strLen = len(s)
        result = []

        wordCountMap = self.removeDup(words)
        wordsCount = len(wordCountMap)

        memo = {}
        wordLimit = { }
        allIndexes = set()
        index = -1
        for entry in wordCountMap.items():
            index += 1
            w = entry[0]
            wordLimit[index] = entry[1]
            occurrences = [m.start() for m in re.finditer('(?=' + w + ')', s)] #StrAux.strStr(s, w)
            for o in occurrences:
                memo[o] = index
                allIndexes.add(o)
        
        q = ArrayQueue(fullWordCount)
        allIndexes = sorted(allIndexes)

        for start in range(0, wordLen):
            membership = {}
            violation = 0
            q.clear()

            lastI = -start - 1
            for i in [ _ for _ in allIndexes if _ % wordLen == start]:
                if (i - lastI != wordLen):
                    membership.clear()
                    q.clear()

                wordIndex = memo[i]
                oldStrIndex = q.enqueueAndDequeue(i)

                if (wordIndex in membership):
                    if (membership[wordIndex] == wordLimit[wordIndex]):
                        violation += 1
                    membership[wordIndex] += 1
                else:
                    membership[wordIndex] = 1
                
                if (oldStrIndex != None):
                    firstWordIndex = memo[oldStrIndex]
                    membership[firstWordIndex] -= 1
                    if (membership[firstWordIndex] == wordLimit[firstWordIndex]):
                        violation -= 1

                if (q.full() and violation == 0):
                    startIndex = q.peak()
                    result.append(startIndex)
                    
                lastI = i

        return result

def test(sln, s, words):
    result = sln.findSubstring(s, words)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "barfoothefoobarman", ["foo","bar"])
    test(sln, "wordgoodgoodgoodbestword", ["word","good","best","word"])
    test(sln, "barfoofoobarthefoobarman", ["bar","foo","the"])
    test(sln, "wordgoodgoodgoodbestword", ["word","good","best","good"])
    test(sln, "aaaa", ["aa","aa"])
    # q = ArrayQueue(3)
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueueAndDequeue(4)

    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.peak())