# problem: https://leetcode-cn.com/problems/WInSav/
# solution:
#     - calculate max layer sum for un-modified tree
#     - create Block for each removeable node. Block could be nested.
#     - Each block contains 0~more inner blocks and 0~more other nodes.
#     - For each block, recursively calculate for each layer following 2 functions:
#         1. diffSums: sum of node value diff for a certain layer within a block
#            diffSums = sum{ block.innerNodes.diffSum } + sum{ block.innerBlocks }
#         2. maxDiff: maximum node value diff on a certain layer within a block
#            maxDiff = max{ diffSums, block.innerBlocks.maxDiff }
#     - For each node, the "node value diff" is the amound of the difference when its value
#       is replaced with its children's value

from typing import Dict, List, Optional, Tuple
from queue import Queue

class TreeNode:
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r

class Block:
    def __init__(self, r):
        self.root = r
        self.nodes: dict[int, list] = {}
        self.innerBlocks: list[Block] = []
        self.layerDiffSums: dict[int, int] = {}
        self.maxLayerDiff: dict[int, int] = {}
        self.lastLayerNodeCount: int = 0

    def addNode(self, layer, node):
        if layer not in self.nodes:
            self.nodes[layer] = []
        self.nodes[layer].append(node)

    def clearNodes(self):
        self.nodes.clear()

    def addBlock(self, block):
        self.innerBlocks.append(block)

class Solution:
    def getMaxLayerSum(self, root: Optional[TreeNode]) -> int:
        # calculate layer sum for un-modified tree
        layerSums = self._calcLayerSums(root)
        layerCount = len(layerSums)
        # calculate node value diff for each node
        self._dfs_preorder(root, lambda n, l: self._attachReplacementDiff(n))
        # build nested blocks
        blockResult = self._groupPossibleReplacements(root, layerCount)
        # merge block.layerDiffSums and block.maxLayerDiff from inside out
        replacements = self._mergeBlocks(blockResult[0], blockResult[1], layerCount)
        # combine result
        maxLayerSum = self._calcMaxLayerSum(layerSums, replacements)
        return maxLayerSum

    def _calcLayerSums(self, root: Optional[TreeNode]):
        layerSums = []
        self._dfs_preorder(root, lambda n, l: self._populateLayerSum(n, l, layerSums))
        return layerSums

    def _populateLayerSum(self, node: TreeNode, layer: int, layerSums: list):
        if len(layerSums) > layer:
            layerSums[layer] += node.val
        else:
            layerSums.append(node.val)

    def _attachReplacementDiff(self, n: TreeNode):
        value = -n.val
        if n.left != None:
            value += n.left.val
        if n.right != None:
            value += n.right.val
        n.replacementDiff = value

    def _groupPossibleReplacements(self, root: TreeNode, layerCount: int):
        blocks: list[Block] = []
        lastLayerNodes = 0
        stack = [(root, 0, None)]

        while len(stack) > 0:
            e = stack.pop()
            node: TreeNode = e[0]
            layer: int = e[1]
            block: Block = e[2]

            if node.left != None and node.right != None:
                if block != None:
                    block.addNode(layer, node)
            else:
                newBlock = Block(node)
                newBlock.addNode(layer, node)
                if block != None:
                    block.addBlock(newBlock)
                else:
                    blocks.append(newBlock)
                block = newBlock

            if node.right != None:
                stack.append((node.right, layer + 1, block))
            if node.left != None:
                stack.append((node.left, layer + 1, block))

            if layer == layerCount - 1:
                lastLayerNodes += 1

        result = (blocks, lastLayerNodes)
        return result

    def _mergeBlocks(self, blocks: List[Block], lastLayerNodes: int, layerCount: int):
        for rootBlock in blocks:
            stack = [(rootBlock, 0)]

            while len(stack) > 0:
                e = stack.pop()
                block: Block = e[0]
                progress: int = e[1]

                if progress < len(block.innerBlocks):
                    stack.append((block, progress + 1))
                    stack.append((block.innerBlocks[progress], 0))
                else:
                    self._mergeBlock(block, lastLayerNodes, layerCount)

        replaceResult: dict[int, int] = {}
        self._mergeMaxLayerSum(blocks, replaceResult)

        return replaceResult

    def _mergeBlock(self, block: Block, totallastLayerNodeCount: int, layerCount: int):
        layerDiffSums: dict[int, int] = {}
        maxLayerDiff: dict[int, int] = {}
        if len(block.innerBlocks) > 0:
            layerDiffSums = block.innerBlocks[0].layerDiffSums

        # handle the case where last layer is totally removed, if all nodes on last layer are moved upwards.
        lastLayerNodeCount = len(block.nodes.get(layerCount - 1, [])) + sum([b.lastLayerNodeCount for b in block.innerBlocks])
        block.lastLayerNodeCount = lastLayerNodeCount
        containsAllLastLayer = (lastLayerNodeCount == totallastLayerNodeCount)
        containsSingleAllLayerLayer = containsAllLastLayer and (totallastLayerNodeCount == 1)

        for i in range(1, len(block.innerBlocks)):
            ib = block.innerBlocks[i]
            for layer in ib.layerDiffSums:
                value = ib.layerDiffSums[layer]
                self._tryAddSum(layerDiffSums, layer, value)
                
        if block.nodes != None:
            for layer in block.nodes:
                value = sum([n.replacementDiff for n in block.nodes[layer]])
                self._tryAddSum(layerDiffSums, layer, value)
        
        if containsAllLastLayer:
            layerDiffSums.pop(layerCount - 1, None)
        
        maxLayerDiff = layerDiffSums.copy()
        self._mergeMaxLayerSum(block.innerBlocks, maxLayerDiff)

        if containsSingleAllLayerLayer:
            maxLayerDiff.pop(layerCount - 1, None)

        block.layerDiffSums = layerDiffSums
        block.maxLayerDiff = maxLayerDiff
        return

    def _mergeMaxLayerSum(self, blocks: List[Block], maxLayerDiff: Dict[int, int]):
        for i in range(0, len(blocks)):
            block = blocks[i]
            for layer in block.maxLayerDiff:
                value = block.maxLayerDiff[layer]
                if layer in maxLayerDiff:
                    maxLayerDiff[layer] = max(maxLayerDiff[layer], value)
                else:
                    maxLayerDiff[layer] = value

    def _tryAddSum(self, d: Dict[int, int], layer: int, value: int):
        if layer in d:
            d[layer] += value
        else:
            d[layer] = value

    def _calcMaxLayerSum(self, layerSums: List[int], replacements: Dict[int, int]):
        result = -1000000000000

        for layer in range(len(layerSums)):
            originalLayerSum = layerSums[layer]
            diff = replacements.get(layer, 0)
            result = max(result, originalLayerSum, originalLayerSum + diff)

        return result

    def _dfs_preorder(self, root, action):
        stack = [(root, 0)]
        while len(stack) > 0:
            e = stack.pop()
            node = e[0]
            layer = e[1]
            action(node, layer)

            if node.right != None:
                stack.append((node.right, layer + 1))
            if node.left != None:
                stack.append((node.left, layer + 1))
        return

    # partial implementation of a brute force solution for testing
    def _test0(self, root: TreeNode, node: TreeNode):
        t = self._removeable(node.left)
        if t[0]:
            temp = node.left
            node.left = t[1]
            layerSums = self._calcLayerSums(root)
            print("removed " + str(temp.val))
            print(layerSums)
            print("max: " + str(max(layerSums)))
            node.left = temp
        
        t = self._removeable(node.right)
        if t[0]:
            temp = node.right
            node.right = t[1]
            layerSums = self._calcLayerSums(root)
            print("removed " + str(temp.val))
            print(layerSums)
            print("max: " + str(max(layerSums)))
            node.right = temp

        if node.left != None:
            self._test0(root, node.left)

        if node.right != None:
            self._test0(root, node.right)

    def _removeable(self, node: TreeNode):
        if node == None:
            return (False, None)
        r = node.left == None or node.right == None
        c = node.right if node.left == None else node.left
        return (r, c)

    def test(self, root: TreeNode):
        layerSums = self._calcLayerSums(root)
        print("original tree")
        print(layerSums)
        print("max: " + str(max(layerSums)))

        t = self._removeable(root)
        if t[0] and t[1] != None:
            layerSums = self._calcLayerSums(t[1])
            print("removed root")
            print(layerSums)
            print("max: " + str(max(layerSums)))
        
        self._test0(root, root)
        return None

def test(sln, root):
    result = sln.getMaxLayerSum(root)
    print(result)

def test2(sln, root):
    result = sln.test(root)

def buildTree(t: list):
    q = Queue()
    root = TreeNode(t[0], None, None)
    q.put(root)

    i = 1
    while i < len(t):
        node = q.get()
        value = t[i]

        if value != None:
            node.left = TreeNode(value, None, None)
            q.put(node.left)
        
        i += 1
        if i < len(t):
            value = t[i]
            if value != None:
                node.right = TreeNode(value, None, None)
                q.put(node.right)

        i += 1
    
    return root

if __name__ == "__main__":
    sln = Solution()
    test(sln, buildTree([6,0,3,None,8]))
    test(sln, buildTree([5,6,2,4,None,None,1,3,5]))
    test(sln, buildTree([-5,1,7]))
    test(sln, buildTree([-1,None,-2,None,-3,None,-4,None,-5,None,-6]))
    test(sln, buildTree([-10,-8,3,-5,-2,None,-1]))
    test(sln, buildTree([6,7,3,6,None,2,None,5,4,99,None,100,50,None,None,1]))
    test(sln, buildTree([13,97,4,-20,None,None,15,-60,-20,100,200]))
    test(sln, buildTree([-20,-9,None,-18,-7,-5,None,-5,-19,-13,-4,-8,None,-10,-4,-14,-18,-14,None,None,66,-8,-20,None,-16,-15,-19,-13,-2,73,55,None,None,-2,-10,4,-4,3,-11,-20,33,2,-5,-8,-9,-9,-15,None,None,None,None,None,-5,90,None,None,None,-5,-6,None,None,-4,None,5,None,None,None,None,None,-14,None,-3,None,-5,41,-2,-17,90,-11,None,None,None,None,-12,-18,-4,-3,83,7,None,None,None,-13,-19,None,None,51,None,None,-3,-20,-11,-17,None,None,-6,None,-17,-5,50,-6,-11,None,57,None,None,None,None,None,None,None,-3,None,None,None,None,None,None,None,-18,-11,-18,None,None,None,None,None,90,None,None,None,-13,-3,None,None,None,None,17,80,-20,-7,-9,-6,None,None,None,None,-14,None,-7,67,None,None,None,None,None,52,None,-1,18,31,-7,None,None,None,None,None,None,None,None,None,22,None,None,None,None,None,None,38]))

    # test(sln, TreeNode(5, 
    #             TreeNode(6, 
    #                 TreeNode(4, 
    #                     TreeNode(3, None, None), 
    #                     TreeNode(5, None, None)), 
    #                 None), 
    #             TreeNode(2, 
    #                 None, 
    #                 TreeNode(1, None, None))))
    # test(sln, TreeNode(6, 
    #             TreeNode(0, 
    #                 None, 
    #                 TreeNode(8, None, None)), 
    #             TreeNode(3, None, None)))
    # test(sln, TreeNode(-5, 
    #             TreeNode(1, None, None), 
    #             TreeNode(7, None, None)))

    # test(sln, TreeNode(-1, None, 
    #             TreeNode(-2, None, 
    #                 TreeNode(-3, None, 
    #                     TreeNode(-4, None, 
    #                         TreeNode(-5, None, 
    #                             TreeNode(-6, None, None)))))))

    # test(sln, TreeNode(-10, 
    #             TreeNode(-8, 
    #                 TreeNode(-5, None, None), 
    #                 TreeNode(-2, None, None)), 
    #             TreeNode(3, 
    #                 None, 
    #                 TreeNode(-1, None, None))))

    # test(sln, TreeNode(6, 
    #             TreeNode(7, 
    #                 TreeNode(6, 
    #                     TreeNode(5, 
    #                         TreeNode(100, None, None), 
    #                         TreeNode(50, None, None)), 
    #                     TreeNode(4, None, None)), 
    #                 None), 
    #             TreeNode(3, 
    #                 TreeNode(2, 
    #                     TreeNode(99, 
    #                         TreeNode(1, None, None), 
    #                         None), 
    #                     None), 
    #                 None)))

    # test(sln, TreeNode(13, 
    #             TreeNode(97, 
    #                 TreeNode(-20, 
    #                     TreeNode(-60, None, None), 
    #                     TreeNode(-20, None, None)), 
    #                 None), 
    #             TreeNode(4, 
    #                 None, 
    #                 TreeNode(15, 
    #                     TreeNode(100, None, None),  
    #                     TreeNode(200, None, None)))))