class TodoList:
    # add tasks, mark as complete, get non-complete tasks
    # add tags to task, get tags with task

    # task has user, tid, descr, duedate, tags, completed
    # we need to sort by duedate,
    # filter by task, userId

    # we can just remove completed tasks

    # map: user -> tasks: (duedate, tid, decr)
    # map: tag -> set of tids with the tag
    # to mark completed, just remove from userSet

    def __init__(self):
        self.tasks = defaultdict(set) # user -> set of tasks: (duedate, tid, decr) (set for fast removal)
        self.tagSets = defaultdict(set) # tag -> set of tids with the tag
        self.tCount = 1
        self.tidToUser = {} # maps tid -> userId, (duedate, tid, descr), so that when we delete, we know immediately which user set
        

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        # add task to a user 
        # returns taskId (1,2,3...)
        tid = self.tCount
        self.tCount += 1
        newTask = (dueDate, tid, taskDescription)
        self.tasks[userId].add(newTask)
        self.tidToUser[tid] = (userId, newTask)
        
        for tag in tags:
            self.tagSets[tag].add(tid)
        return tid
    

    def getAllTasks(self, userId: int) -> List[str]:
        # get all tasks not complete for a user, ordered by due date
        taskList = list(self.tasks[userId])
        taskList.sort()
        return [t[2] for t in taskList] # only a list of descriptions
        

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        # same as above, but filter only some tags
        tasksWithTag = self.tagSets[tag]

        taskList = [t for t in self.tasks[userId] if t[1] in tasksWithTag]
        taskList.sort()
        return [t[2] for t in taskList] # only a list of descriptions
        

    def completeTask(self, userId: int, taskId: int) -> None:
        if taskId not in self.tidToUser: # make sure task exists
            return
        actualUserId, delTask = self.tidToUser[taskId]
        if actualUserId != userId: # the user actually has the task
            return
        if delTask in self.tasks[userId]: # make sure not completed yet
            self.tasks[userId].remove(delTask)

        
        


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)