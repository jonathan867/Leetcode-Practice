class UndergroundSystem:
    # list of times a -> b: (start, end) -> list of times
    # id checks in at station
    # id checks out -> need their start, populate start, end, time

    def __init__(self):
        self.riding = {} # people who are still in the system: id -> (start, time)
        self.pathTimes = defaultdict(list) # (start, end) -> list of times
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.riding[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startS, startT = self.riding[id]
        del self.riding[id]
        self.pathTimes[(startS, stationName)].append(t - startT)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.pathTimes[(startStation, endStation)]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)