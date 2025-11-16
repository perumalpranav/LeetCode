class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        #CHATGPT, I STILL DONT GET IT

        n = len(favorite)
        indegree = [0] * n
        
        for f in favorite:
            indegree[f] += 1
        
        # queue: remove all nodes not in cycles
        from collections import deque
        q = deque()
        dist = [0] * n
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            y = favorite[x]
            indegree[y] -= 1
            dist[y] = max(dist[y], dist[x] + 1)
            if indegree[y] == 0:
                q.append(y)
        
        visited = [0] * n
        longest_cycle = 0
        mutual_sum = 0
        
        for i in range(n):
            if indegree[i] == 0:
                continue  # not in a cycle
            
            cur = i
            length = 0
            while visited[cur] == 0:
                visited[cur] = 1
                cur = favorite[cur]
                length += 1
            
            # length of a true cycle
            if length == 2:
                # mutual pair: a <-> b
                a = i
                b = favorite[i]
                mutual_sum += 2 + dist[a] + dist[b]
            else:
                longest_cycle = max(longest_cycle, length)
        
        return max(longest_cycle, mutual_sum)
