from typing import List
from math import ceil

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        startIndex = 0
        size = len(words)
        result = []

        while True:
            endIndex = self.getNextLine(words, startIndex, maxWidth)
            
            if endIndex == size:
                result.append(self.justifyLeft(words, startIndex, endIndex, maxWidth))
                return result
            else:
                result.append(self.justifyFully(words, startIndex, endIndex, maxWidth))
                startIndex = endIndex

    def getNextLine(self, words: List[str], start: int, maxWidth: int):
        maxWidth -= len(words[start])
        while maxWidth >= 0:
            start += 1
            if start == len(words):
                break
            maxWidth = maxWidth - len(words[start]) - 1

        return start

    def justifyLeft(self, words: List[str], start: int, end: int, maxWidth: int):
        line = words[start]
        maxWidth -= len(words[start])

        for i in range(start + 1, end):
            w = words[i]
            line = line + " " + w
            maxWidth = maxWidth - len(w) - 1

        line += (" " * maxWidth)
        return line

    def justifyFully(self, words: List[str], start: int, end: int, maxWidth: int):
        line = words[start]

        spaceWidth = maxWidth
        for i in range(start, end):
            spaceWidth -= len(words[i])

        wordCount = end - start - 1
        for i in range(start + 1, end):
            w = words[i]
            spaces = ceil(spaceWidth / wordCount)
            line = line + (" " * spaces) + w
            spaceWidth = spaceWidth - spaces
            wordCount -= 1

        if spaceWidth > 0:
            line += (" " * spaceWidth)

        return line

def test(sln, words, maxWidth):
    result = sln.fullJustify(words, maxWidth)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, ["This", "is", "an", "example", "of", "text", "justification."], 16)
    test(sln, ["What","must","be","acknowledgment","shall","be"], 16)
    test(sln, ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)