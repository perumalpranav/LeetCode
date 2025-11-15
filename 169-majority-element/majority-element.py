from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        maj = None
        for n in nums:
            if counter == 0:
                maj = n
            if maj == n:
                counter += 1
            else:
                counter -= 1
        return maj


