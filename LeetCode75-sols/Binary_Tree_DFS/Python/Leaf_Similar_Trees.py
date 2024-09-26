from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_values(node):
            leaf_values = []
            def dfs(current_node):
                if current_node:
                    if not current_node.left and not current_node.right:
                        # This is a leaf
                        leaf_values.append(current_node.val)
                    else:
                        # Traverse left and ride to children
                        dfs(current_node.left)
                        dfs(current_node.right)
            dfs(node)
            return leaf_values
        leaves1 = get_leaf_values(root1)
        leaves2 = get_leaf_values(root2)

        return leaves1 == leaves2
