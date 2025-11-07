from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt = list(cnt.items())
        cnt = sorted(cnt, key=lambda x: x[1], reverse=True)

        ans = [] 
        for _, item in zip(range(k), cnt):
            ans.append(item[0])

        return ans