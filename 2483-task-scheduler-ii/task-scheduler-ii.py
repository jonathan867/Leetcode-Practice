class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        taskHist = {} # task number -> day it was last done

        i = 0
        days = 0

        while i < len(tasks):
            tType = tasks[i]

            if tType not in taskHist or days - taskHist[tType] > space:
                days += 1
                taskHist[tType] = days
                # print(i)
            else: # we need to wait
                timeWaited = days - taskHist[tType]
                addWait = space - timeWaited + 1
                
                days += addWait
                taskHist[tType] = days # update the history
                # print(i, timeWaited, addWait, days)
            i += 1

        return days
        