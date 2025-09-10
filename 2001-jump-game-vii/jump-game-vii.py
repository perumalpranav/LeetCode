from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #dp[i] = is it possible to reach place i
        n = len(s)
        s = list(s)

        if minJump >= n:
            return False

        dq = deque([])
        dsum = 0
        windowlen = maxJump - minJump + 1

        for i in range(1,n):
            if windowlen == len(dq):
                index = dq.popleft()
                dsum -= 1 if s[index] == '0' else 0

                if i-minJump < n and i-minJump >= 0:
                    dq.append(i-minJump)
                    dsum += 1 if s[i-minJump] == '0' else 0
            else:
                if i-minJump < n and i-minJump >= 0:
                    dq.append(i-minJump)
                    dsum += 1 if s[i-minJump] == '0' else 0
            
            #print(f"This {dq}, {dsum}, {i}")
            if len(dq) > 0 and dsum > 0 and s[i] == '0':
                s[i] = '0'
            else:
                s[i] = '1'

        print(s)
        return s[-1] == '0'