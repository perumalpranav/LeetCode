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
        
        #Better Solution
        #Traverse tree looking for the nodes
        #If a node is > one but < other, this is the last common ancestor
        #Else, continue if they agree in one direction

        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr


        return None

