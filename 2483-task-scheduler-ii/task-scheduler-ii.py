class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        taskHist = {} # task number -> day it was last done

        i = 0
        days = 1

        while i < len(tasks):
            tType = tasks[i]

            if tType not in taskHist:
                taskHist[tType] = days
                days += 1
            else:
                timeWaited = days - taskHist[tType]
                if timeWaited > space: # immediatly do task
                    taskHist[tType] = days
                    days += 1
                else: # wait until timeWaited is big enough
                    # 3 - 1 -> 2, 2 = 3 - 2 + 1
                    addWait = space - timeWaited + 1
                    days += addWait
                    taskHist[tType] = days # update the history
                    days += 1 # get to the next day
            i += 1

        return days - 1
        