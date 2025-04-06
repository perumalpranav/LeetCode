"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        completedNodes = {}
        def dfs(originalNode):
            completedNodes[originalNode.val] = Node(originalNode.val)
            for neighbor in originalNode.neighbors:
                if neighbor.val not in completedNodes.keys():
                    dfs(neighbor)

                completedNodes[originalNode.val].neighbors.append(completedNodes[neighbor.val])

        dfs(node)
        return completedNodes[node.val]

        