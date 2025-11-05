# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs returns number of matches (p or q). first one to have matches == 2 is the answer

        self.ans = None

        def dfs(node): # returns number of matches
            if not node: # early breakout if ans found (nevermind, doing early breakout is wrong?)
                return 0
            
            matches = 0
            if node.val == p.val or node.val == q.val:
                matches += 1
            matches += dfs(node.left)
            matches += dfs(node.right)

            if matches == 2:
                if not self.ans:
                    self.ans = node
            
            return matches
        
        dfs(root)
        return self.ans
