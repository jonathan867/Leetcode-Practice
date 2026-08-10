class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # find the largest and smallest, move into a set, and then look for everything in between

        maxN, minN = max(nums), min(nums)

        s = set(nums)
        ans = []
        for i in range(minN, maxN+1):
            if i not in s:
                ans.append(i)
        
        print(ans)
        return ans