from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        lastVisited = None
        left = None; right = None

        for n in self._traverse(root):
            value = n.val
            if lastVisited != None and value < lastVisited.val:
                if left == None:
                    left = lastVisited
                right = n
            
            lastVisited = n

        print(left.val)
        print(right.val)

        temp = left.val
        left.val = right.val
        right.val = temp

    # in-order traverse which uses O(1) space
    def _traverse(self, node: Optional[TreeNode]):
        while node != None:
            if node.left == None:
                yield node
                node = node.right
            else:
                t = node.left
                while t.right != None and t.right != node:
                    t = t.right

                if t.right == node:
                    t.right = None
                    yield node
                    node = node.right
                else:
                    t.right = node
                    node = node.left

def test(sln, root):
    sln.recoverTree(root)

if __name__ == "__main__":
    sln = Solution()
    test(sln, TreeNode(1, TreeNode(3, None, TreeNode(2))))
    test(sln, TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2))))