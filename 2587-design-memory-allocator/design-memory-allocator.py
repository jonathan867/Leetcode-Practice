class Allocator:
    # we can have a free table and used table
    # free: length -> start
    # used: id -> length, start

    def __init__(self, n: int):
        # self.free = {0:n} # start -> length
        self.free = [[0, n]] # this needs to be sorted, so lets just use an arr
        self.used = defaultdict(list) # id -> list of (length, start)
        

    def allocate(self, size: int, mID: int) -> int:
        for start, l in self.free: # find first with right size
            if l >= size:
                self.used[mID].append([size, start])
                self.free.remove([start, l])
                if l > size: # create a new free block
                    newStart = start + size
                    newLen = l - size
                    bisect.insort(self.free, [newStart, newLen])
                return start
        return -1  


    def freeMemory(self, mID: int) -> int:
        memCount = 0
        for l, start in self.used[mID]:
            bisect.insort(self.free, [start, l])
            memCount += l
        del self.used[mID]
        # coalesce
        i = 1
        while i < len(self.free):
            start, l = self.free[i]
            prevStart, prevL = self.free[i-1]
            if start == prevStart + prevL: # need to join blocks
                self.free[i-1][1] += l
                self.free.pop(i) # remove 2nd block
            else:
                i += 1
        
        return memCount

# 23:46


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)