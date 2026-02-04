"""
Maximum Depth Of Binary Tree Problem

Clean single-entry implementation surface.
"""

from typing import Optional, Any


class Solution:
    def solve(self, root: Optional[Any]) -> int:
        """
        Implement the Maximum Depth of Binary Tree solution here.

        Args:
            root: Optional[TreeNode]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def maximum_depth_of_binary_tree(root: Optional[Any]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(root)


if __name__ == "__main__":
    pass
