class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        start = 0
        flips = 0
        currentlyflipped = 0


        while start < n:
            if nums[start] >= 2:
                nums[start] -= 2
                currentlyflipped ^= 1
            
            if (nums[start] ^ currentlyflipped) == 0:
                if start + k > n:
                    #If we try to flip something but can't because k is too big
                    return -1
                flips += 1
                currentlyflipped ^= 1
                if start + k < n:
                    nums[start + k] += 2
            
            start += 1
        
        return flips
        