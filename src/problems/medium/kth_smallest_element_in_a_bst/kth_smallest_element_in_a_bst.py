"""
Kth Smallest Element In A Bst Problem

Clean single-entry implementation surface.
"""

from typing import Optional, Any


class Solution:
    def solve(self, root: Optional[Any], k: int) -> int:
        """
        Implement the Kth Smallest Element in a BST solution here.

        Args:
            root: Optional[TreeNode]
            k: int

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def kth_smallest_element_in_a_bst(root: Optional[Any], k: int) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(root, k)


if __name__ == "__main__":
    pass
