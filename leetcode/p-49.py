from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = str(sorted(word))
            if (key in groups):
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())

def test(sln, strs):
    result = sln.groupAnagrams(strs)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, ["eat","tea","tan","ate","nat","bat"])
    test(sln, [""])
    test(sln, ["a"])