from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return "[" + str(self.val) + ", " + str(self.left) + ", " + str(self.right) + "]"
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = [0, 0] # index into pre-order and in-order list

        return self._buildTree(preorder, inorder, indices, None)

    def _buildTree(self, preorder: List[int], inorder: List[int], indices: list, end: int):
        value = preorder[indices[0]]
        r = TreeNode(value)

        # start of in-order and pre-order mismatch, therefore there is left sub-tree
        if value != inorder[indices[1]]:
            indices[0] += 1
            r.left = self._buildTree(preorder, inorder, indices, value)
            indices[1] += 1

        # right sub-tree exists
        if (indices[0] < len(preorder) - 1) and (end == None or end != inorder[indices[1] + 1]):
            indices[0] += 1
            indices[1] += 1
            r.right = self._buildTree(preorder, inorder, indices, end)

        return r

def test(sln, preorder, inorder):
    result = sln.buildTree(preorder, inorder)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [3,9,20,15,7], [9,3,15,20,7])
    test(sln, [1,2,4,5,3,6,7], [4,2,5,1,6,3,7])