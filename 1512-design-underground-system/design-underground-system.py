class UndergroundSystem:

    def __init__(self):
        self.paths = {} #key: x,y value: avg time, divisor
        self.checkedIn = {} #key id, value: station, time

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName,t)
        #ID SHOULD always not exist

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedIn.pop(id)
        path = (startStation, stationName)
        if path in self.paths.keys():
            avg, divisor = self.paths[path]
            avg = ((avg * divisor) + (t - startTime))/(divisor+1)
            self.paths[path] = (avg, divisor + 1)
        else:
            self.paths[path] = ((t - startTime), 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        path = (startStation, endStation)
        return self.paths[path][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)