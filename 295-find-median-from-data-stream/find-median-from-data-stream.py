import bisect

class MedianFinder:

    def __init__(self):
        self.datalist = []
        self.medianIndex = -1
        self.length = 0
        
    def addNum(self, num: int) -> None:
        loc = bisect.bisect_left(self.datalist, num)
        self.datalist.insert(loc, num)
        if self.length % 2 == 0:
            self.medianIndex += 1
        self.length += 1

        

    def findMedian(self) -> float:
        if self.medianIndex == -1:
            return None
        else:
            if self.length % 2 == 0:
                return (self.datalist[self.medianIndex] + self.datalist[self.medianIndex + 1])/2
            else:
                return self.datalist[self.medianIndex]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()