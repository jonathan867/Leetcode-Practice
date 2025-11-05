class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # (pre, post)

        # course -> courses it is a prereq for (post)
        prereqs = defaultdict(set)
        # course -> number of prereqs it has 
        prqCount = defaultdict(int)

        # 1. build the 2 dicts
        for post, pre in prerequisites:
            prereqs[pre].add(post)
            prqCount[post] += 1
            if pre not in prqCount: # make sure all courses in the pairs are in preqCount
                prqCount[pre] = 0

        
        # bfs start with the courses with no prereqs
        noPrqs = []
        for c, count in prqCount.items():
            if count == 0:
                noPrqs.append(c)
        
        # bfs
        q = deque(noPrqs)
        visited = set(noPrqs)
        ans = []

        while q:
            cur = q.popleft() # we know cur is a reachable course
            ans.append(cur)
            for post in prereqs[cur]: # all the post courses that cur helps "unlock"
                prqCount[post] -= 1
                if prqCount[post] <= 0 and post not in visited: # this post is also valid
                    q.append(post)
                    visited.add(post)
        
        # check if all courses reachable
        if len(ans) != len (prqCount):
            return []
        
        # search for courses that are have no relationships
        noRel = []
        for i in range(numCourses):
            if i not in prqCount:
                noRel.append(i)

        ans.extend(noRel)
        return ans
                

