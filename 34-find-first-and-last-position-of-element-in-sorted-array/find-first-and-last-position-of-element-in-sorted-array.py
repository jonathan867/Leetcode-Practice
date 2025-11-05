class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # lets try doing the manual bsLE and bsGE

        # nums = [8,8,8,8,8,8]

        def bsLE(targ, nums): # returns the greatest (rightmost) element that is LE targ
            l, r = 0, len(nums)-1
            ind = -1

            while l <= r:
                m = (l+r) // 2
                if nums[m] <= targ:
                    ind = m
                    l = m+1
                else:
                    r = m-1
            return ind
            
        def bsGE(targ, nums): # returns the smallest (leftmost) element that is GE targ
            l, r = 0, len(nums)-1
            ind = -1

            while l <= r:
                m = (l+r) // 2
                if nums[m] >= targ:
                    ind = m
                    r = m-1
                else:
                    l = m+1
            return ind
        
        ind1 = bsGE(target, nums)
        ind2 = bsLE(target, nums)
        if ind1 == -1 or ind2 == -1 or not(nums[ind1] == nums[ind2] == target):
            return [-1, -1]
        return [ind1, ind2]

