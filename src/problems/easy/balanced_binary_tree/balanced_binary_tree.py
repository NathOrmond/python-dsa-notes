"""
Balanced Binary Tree Problem

Clean single-entry implementation surface.
"""

from typing import Optional, Any


class Solution:
    def solve(self, root: Optional[Any]) -> bool:
        """
        Implement the Balanced Binary Tree solution here.

        Args:
            root: Optional[TreeNode]

        Returns:
            bool
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def balanced_binary_tree(root: Optional[Any]) -> bool:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(root)


if __name__ == "__main__":
    pass
