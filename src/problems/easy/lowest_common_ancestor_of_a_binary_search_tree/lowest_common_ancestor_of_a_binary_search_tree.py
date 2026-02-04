"""
Lowest Common Ancestor Of A Binary Search Tree Problem

Clean single-entry implementation surface.
"""

from typing import Optional, Any


class Solution:
    def solve(self, root: Optional[Any], p: Any, q: Any) -> Optional[Any]:
        """
        Implement the LCA of a BST solution here.

        Args:
            root: Optional[TreeNode]
            p: TreeNode
            q: TreeNode

        Returns:
            Optional[TreeNode]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def lowest_common_ancestor_of_a_binary_search_tree(root: Optional[Any], p: Any, q: Any) -> Optional[Any]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(root, p, q)


if __name__ == "__main__":
    pass
