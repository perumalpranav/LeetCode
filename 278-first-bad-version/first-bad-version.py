# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n

        while lo < hi:
            check = (lo + hi) // 2
            if isBadVersion(check):
                hi = check
            else:
                lo = check + 1
        
        return lo