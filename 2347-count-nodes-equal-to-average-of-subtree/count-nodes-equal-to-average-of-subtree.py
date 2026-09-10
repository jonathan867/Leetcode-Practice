# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # you need the sum of each subtree. get the sum of the left, sum of the right, + curNode and take avg
        ans = 0

        def dfs(node): # returns subtree sum, and subtree count of nodes
            nonlocal ans

            # dfs and get the sum of each subtree
            if not node:
                return 0, 0

            lSum, lCount = dfs(node.left)
            rSum, rCount = dfs(node.right)

            subtreeSum = lSum + rSum + node.val
            subtreeCount = lCount + rCount + 1

            if int(subtreeSum / subtreeCount) == node.val:
                ans += 1

            return subtreeSum, subtreeCount

        dfs(root)
        return ans

# 5:51
# TC: O(n), all nodes visited once