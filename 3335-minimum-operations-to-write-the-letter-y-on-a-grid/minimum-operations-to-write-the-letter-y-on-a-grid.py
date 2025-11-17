class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        # the cost for each possible solution is 
        # 3 choices: cost of making Ycells 0, 1, 2
        # 2 further choices: cost of making non-Ycells 0, 1, 2

        # first, find all counts for yCells, non yCells
        # num -> frq

        # the cost for making all yCells 0 is frq 1 + frq 2
        
        # lets just mark all the y cell coords first
        n = len(grid)
        yCells = set() # set of coords

        
        for i in range(n//2 + 1): # for n=5, we need to get to index 2
            yCells.add((i, i)) # first diag
            yCells.add((i, n-1-i)) # second diag
        # middle vertical
        for i in range(n//2, n): # for n=5, we do (2 to 4)
            yCells.add((i, n//2))
        print(yCells)

        # iter through grid, get frqs
        yFrq = defaultdict(int) # num -> frq
        notYFrq = defaultdict(int)

        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                if (i,j) in yCells:
                    yFrq[num] += 1
                else:
                    notYFrq[num] += 1
        
        costSetY = {}
        costSetY[0] = yFrq[1] + yFrq[2]
        costSetY[1] = yFrq[0] + yFrq[2]
        costSetY[2] = yFrq[1] + yFrq[0]

        costSetNotY = {}
        costSetNotY[0] = notYFrq[1] + notYFrq[2]
        costSetNotY[1] = notYFrq[0] + notYFrq[2]
        costSetNotY[2] = notYFrq[1] + notYFrq[0]

        # check all possible total costs
        minCost = float('inf')

        for i in range(3):
            for j in range(3):
                if i == j: # its not valid to set both to the same num
                    continue
                minCost = min(minCost, costSetY[i] + costSetNotY[j])
        return minCost
                



        

        