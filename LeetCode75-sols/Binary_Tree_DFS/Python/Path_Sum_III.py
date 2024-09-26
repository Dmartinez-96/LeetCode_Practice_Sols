from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            num_paths = prefix_sums[curr_sum - targetSum]
            prefix_sums[curr_sum] += 1
            num_paths += dfs(node.left, curr_sum)
            num_paths += dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1
            return num_paths
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        return dfs(root, 0)
