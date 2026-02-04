"""
Binary Tree Right Side View Problem

Clean single-entry implementation surface.
"""

from typing import List, Optional, Any


class Solution:
    def solve(self, root: Optional[Any]) -> List[int]:
        """
        Implement the Binary Tree Right Side View solution here.

        Args:
            root: Optional[TreeNode]

        Returns:
            List[int]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def binary_tree_right_side_view(root: Optional[Any]) -> List[int]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(root)


if __name__ == "__main__":
    pass
