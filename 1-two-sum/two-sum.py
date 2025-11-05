from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(set)
        for i, n in enumerate(nums):
            nums_dict[n].add(i)

        for n in nums_dict.keys():
            complement = target - n
            if complement == n:
                if len(nums_dict[n]) >= 2:
                    return [nums_dict[n].pop(), nums_dict[n].pop()]

            elif complement in nums_dict.keys():
                return [nums_dict[n].pop(), nums_dict[complement].pop()]

        return None
