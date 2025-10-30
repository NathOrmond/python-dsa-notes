"""
Validate Binary Search Tree Problem

Clean single-entry implementation surface.
"""

from typing import Any


class Solution:
    def solve(self, root: Any) -> bool:
        """
        Implement the Validate Binary Search Tree solution here.

        Args:
            root: Tree root node

        Returns:
            bool
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def validate_binary_search_tree(root: Any) -> bool:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(root)


if __name__ == "__main__":
    pass
