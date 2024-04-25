class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        i = 0
        ndict = {}
        for i in range(len(nums)):
            x = ndict.setdefault(nums[i], 0)
            ndict[nums[i]] = x+1
        nums = []

        for key in ndict.keys():
            nums.append((key,ndict[key]))
        
        print(nums)
        for i in range(len(nums)):
            self.insert(nums[i],heap)

        output = []
        print(heap)
        for i in range(k):
            t = self.extract(heap)
            output.append(t[0])

        return output
        
    def insert(self, value, heap):
        heap.append(value)
        self.bubble_up((len(heap) - 1),heap)

    def extract(self, heap):
        if not heap:
            return None
        max_value = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        if heap:
            self.bubble_down(0,heap)
        return max_value

    def bubble_up(self, index, heap):
        parent_index = (index - 1) // 2
        if parent_index < 0:
            return
        if heap[parent_index][1] < heap[index][1]:
            heap[parent_index], heap[index] = heap[index], heap[parent_index]
            self.bubble_up(parent_index,heap)

    def bubble_down(self, index, heap):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        max_index = index
        if left_child_index < len(heap) and heap[left_child_index][1] > heap[max_index][1]:
            max_index = left_child_index
        if right_child_index < len(heap) and heap[right_child_index][1] > heap[max_index][1]:
            max_index = right_child_index
        if max_index != index:
            heap[index], heap[max_index] = heap[max_index], heap[index]
            self.bubble_down(max_index,heap)