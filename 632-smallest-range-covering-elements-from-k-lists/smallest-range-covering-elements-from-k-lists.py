class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # they are all in sorted order.
        # lets start with all first elements. stored as (num, which list its from)
        # store those in a minheap, and also track the max element seen
        # then, each time, try poping away the smallest, and then adding the next from that list.
        # does it make the range better? or does the new one from that list increase the max?
        # when any of the lists are done, you can stop exploring options

        curMax = float('-inf')
        k = len(nums) # number of lists
        nextPs = {i:1 for i in range(k)} # for each list, we have a pointer for the next element to try (smallest)
        # print(nextPs)
        
        h = [] # heap that stores one from each list (value, lInd)
        for i in range(k):
            curMax = max(curMax, nums[i][0])
            heapq.heappush(h, (nums[i][0], i)) # start with the first of each list
        
        # curMin, lInd = h[0]

        bestInt = [float('-inf'), float('inf')] # best range is bestInt[1] - bestInt[0]

        while True: # break when a list's pointer goes out of range
            curMin, lInd = heapq.heappop(h)
            if curMax - curMin < bestInt[1] - bestInt[0]:
                bestInt = [curMin, curMax]
            
            # we need to add in a new element from the same list
            targList = nums[lInd]
            listP = nextPs[lInd]
            if listP >= len(targList): # a list ran out. done exploring
                break
            
            newNum = targList[listP]
            nextPs[lInd] += 1 # move that list's pointer up

            curMax = max(curMax, newNum)
            heapq.heappush(h, (newNum, lInd))
        
        return bestInt

            
# 22:35
# takes a lot of thinking bruh