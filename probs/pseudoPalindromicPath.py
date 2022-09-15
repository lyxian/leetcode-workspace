# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
# 
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

from typing import Optional
class Tree:
    def __init__(self, values=None):
        if values:
            self.root = TreeNode(values[0])
            for value in values[1:]:
                self.insert(value)
        else:
            self.root = TreeNode()

    def insert(self, val):
        # Down > Top , Left > Right
        queue = [self.root]
        while len(queue):
            currNode = queue[0]
            queue.pop(0)

            if currNode.left is None:
                currNode.left = TreeNode(val)
                break
            else:
                queue += [currNode.left]

            if currNode.right is None:
                currNode.right = TreeNode(val)
                break
            else:
                queue += [currNode.right]
    
    def clearNull(self):
        # Down > Top , Left > Right
        queue = [self.root]
        while len(queue):
            currNode = queue[0]
            queue.pop(0)

            if currNode.left:
                if currNode.left.val:
                    queue += [currNode.left]
                else:
                    currNode.left = None

            if currNode.right:
                if currNode.right.val:
                    queue += [currNode.right]
                else:
                    currNode.right = None

    def displayFlat(self):
        def helper(node):
            if node.left:
                helper(node.left)
            print(node.val, end=' ')
            if node.right:
                helper(node.right)
        print('In Order: ', end='')
        helper(self.root)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # Get all path to leaf > Check pseudo-palindromic
        tree = Tree(root)
        tree.clearNull()
        # tree.displayFlat(); print()
        self.count = 0
        self.array = {_: 0 for _ in range(9)}
        def isPP(array):
            odds = evens = 0
            for i in range(9):
                if array[i]:
                    if array[i] % 2:
                        odds += 1
                    else:
                        evens += 1
            return odds < 2

        def helper(node, array):
            if node is None:
                return
            array[node.val-1] += 1
            if node.left is None and node.right is None:   # At leaf
                if isPP(array):
                    self.count += 1
                array[node.val-1] -= 1
                return
            else:
                helper(node.left, array)
                helper(node.right, array)
                array[node.val-1] -= 1
                return

        def showPath(node, path, array):
            if node is None:
                return
            array[node.val-1] += 1
            if node.left is None and node.right is None:   # At leaf
                print(path + [node.val], '\n └─', array)
                if isPP(array):
                    self.count += 1
                array[node.val-1] -= 1
                return
            else:
                showPath(node.left, path + [node.val], array)
                showPath(node.right, path + [node.val], array)
                array[node.val-1] -= 1
                return
        if self.verbose:
            showPath(tree.root, [], [0]*9)
        else:
            helper(tree.root, [0]*9)
        return self.count

if __name__ == '__main__':
    nodes = [2,3,1]
    nodes = [2,3,1,3,1,None,1]
    nodes = [2,1,1,1,3,None,None,None,None,None,1]
    # nodes = [1,9,1,None,1,None,1,None,None,7,None,None,4]

    # tree = Tree(nodes)
    # tree.clearNull()
    # tree.displayFlat()
    print(Solution(True).pseudoPalindromicPaths(nodes))