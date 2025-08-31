# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque()
        q.append(root)
        answers = [root.val]

        def bfs(node):
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            q.popleft()
            return node.val
            
        # Queues children of root node  
        bfs(q[0])
        while len(q) > 0:
            levelsum = 0
            num_nodes = len(q)
            for _ in range(num_nodes):
                # For Loop because it fixes the # of iterations
                # Thus only iterates for the children of the previous level
                levelsum += bfs(q[0])
            levelsum /= num_nodes
            answers.append(levelsum)

        return answers
            
                



