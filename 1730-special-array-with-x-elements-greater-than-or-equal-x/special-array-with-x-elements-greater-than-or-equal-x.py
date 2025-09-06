import bisect

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        x = 1
        while x <= n: #Binary search this too?
            pos = bisect.bisect_left(nums, x)
            print(f"Pos: {pos}, x: {x}")
            if n - pos == x:
                return x
            
            x += 1

        return -1
            