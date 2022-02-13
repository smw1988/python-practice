class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = filter(lambda s: s != "", path.split("/"))
        effectiveParts = []
        for p in parts:
            if p == ".": continue
            elif p == "..":
                if len(effectiveParts) > 0:
                    effectiveParts.pop()
            else:
                effectiveParts.append(p)
        
        return "/" + "/".join(effectiveParts)

def test(sln, path):
    result = sln.simplifyPath(path)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "/home/")
    test(sln, "/../")
    test(sln, "/home//foo/")
    test(sln, "/a/./b/../../c/")
    test(sln, "/")
