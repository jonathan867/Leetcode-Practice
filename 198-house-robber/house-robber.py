class Solution:
    def rob(self, nums: List[int]) -> int:
        # what if there is only one house? 2?
        arr = [0, nums[0]] # index is if you consider 0 houses, 1 house, etc.

        for i in range(1, len(nums)): # we already hit the first one
            curHouse = nums[i]
            # should i keep the max of last house or take this one + max of 2 houses ago?
            curMax = max(arr[-1], arr[-2] + curHouse)
            arr.append(curMax)
        print(arr)
        return arr[-1]