"""
Binary Tree Level Order Traversal Problem

Clean single-entry implementation surface.
"""

from typing import List, Optional, Any


class Solution:
    def solve(self, root: Optional[Any]) -> List[List[int]]:
        """
        Implement the Binary Tree Level Order Traversal solution here.

        Args:
            root: Optional[TreeNode]

        Returns:
            List[List[int]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def binary_tree_level_order_traversal(root: Optional[Any]) -> List[List[int]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(root)


if __name__ == "__main__":
    pass
