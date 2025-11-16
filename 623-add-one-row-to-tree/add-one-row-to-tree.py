# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #Simple Solution
        #Find the nodes at depth = depth - 1
        #For each node (parent) at this level, create two children (copies) with val = val
        #Set the left child of parent for the left copy, and set the right child of parent for the right copy

        if depth == 1:
            #Create for the root
            newroot = TreeNode(val)
            newroot.left = root
            return newroot

        q = deque([root])
        height = 1
        while len(q) > 0:
            for _ in range(len(q)):
                node = q.popleft()
                if height == depth - 1:
                    #Add children here
                    l = TreeNode(val)
                    l.left = node.left
                    node.left = l

                    r = TreeNode(val)
                    r.right = node.right
                    node.right = r
                else:
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)

            height += 1

        return root