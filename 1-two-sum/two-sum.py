class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # put nums you see in map. if targ - cur in map, ans found
        # test

        d = {} # num -> ind

        for i in range(len(nums)):
            if (target - nums[i]) in d:
                return [d[target-nums[i]], i]
            d[nums[i]] = i
        
        return [0,0]

# TC: O(n)
# SC: O(n) for dict