# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Basic Solution
        #"Go up" on the side that is deeper in the tree, until the levels are equal.
        #From here continously check if the nodes at the respective levels are the same, if so return
        #Else, go up one level and repeat

        #Steps
        #Traverse tree, (DFS?) to establish the depth of nodes p and q (build a path from root when doing so)
        #Move up using built paths
        
        def dfs(node, path, target):
            if node is None:
                return None

            path.append(node)

            if node.val == target.val:
                return path

            # search left
            left = dfs(node.left, path, target)
            if left:
                return left

            # search right
            right = dfs(node.right, path, target)
            if right:
                return right

            path.pop()  # backtrack
            return None #This was not the node we were looking for

        pInfo = dfs(root,[],p)
        qInfo = dfs(root,[],q)

        if len(pInfo) < len(qInfo):
            qInfo = qInfo[0:len(pInfo)]
        elif len(pInfo) > len(qInfo):
            pInfo = pInfo[0:len(qInfo)]

        for plast, qlast in zip(pInfo[::-1], qInfo[::-1]):
            if plast.val == qlast.val:
                return plast
        
        return None


        

