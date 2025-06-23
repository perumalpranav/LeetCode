from heapq import heappushpop, heapify

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        #Remove n elements
        #Goal:Minimize Left side, Maximize right side, remove n elements

        n = int(len(nums)/3)

        maxHeap = [-1 * x for x in nums[:n]]
        minHeap = nums[2*n:]

        #Identify maximum from first n nums
        heapify(maxHeap)

        #Identify minimum from last n nums
        heapify(minHeap)

        #Stores smallest possible prefix with n elements for nums[0...i] where i >= n and i < 2n
        prefixSums = [sum(nums[:n])] #Sum of (inclusive) nums[0:n-1]
        for i in range(n,2*n):
            removed = -1 * heappushpop(maxHeap, (-1 * nums[i]))
            prefixSums.append(prefixSums[-1] - removed + nums[i])

        #Stores largest possible suffix with n elements for nums[i...] where i > n and i <= 2n
        suffixSums = [sum(minHeap)] #Sum of (inclusive) nums[2n:3n-1]
        for i in reversed(range(n,2*n)):
            removed = heappushpop(minHeap, nums[i])
            suffixSums.append(suffixSums[-1] - removed + nums[i])


        #Now for each combination of non-overlapping prefixes and suffixes,
        #Find the one with the minimum difference
        minDifference = float('inf')
        for p, s in zip(prefixSums, suffixSums[::-1]):
            minDifference = min(minDifference, p - s)

        return minDifference


        #[16,46,43,41,42,14,36,    49,50,28,38,25,17,5,      18,11,14,21,23,39,23]
        #[46,43,42,41,36,16,14    49,50,28,38,25,17,5,      11,14,18,21,23,23,39,]
        

        





