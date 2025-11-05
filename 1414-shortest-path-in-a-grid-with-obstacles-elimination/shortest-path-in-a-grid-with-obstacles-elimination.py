class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs: coords, elimsLeft, steps so far
        rows = len(grid)
        cols = len(grid[0])

        q = deque([((0,0,k),0)]) # state: (x, y, elims), steps
        visited = set([(0,0,k)]) # x, y, elims

        # print(q.popleft())
        while q:
            (i, j, elims), steps = q.popleft()
            if (i, j) == (rows-1, cols-1): # reached the dest
                return steps

            dirs = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for x, y in dirs:
                if (0<=x<rows and 0<=y<cols):
                    nextElims = elims - grid[x][y]
                    if nextElims < 0: # no more elims to spend. can't move here
                        continue

                    newState = (x, y, nextElims)
                    if newState not in visited:
                        q.append((newState, steps + 1))
                        visited.add(newState)
        return -1
            


                        

        