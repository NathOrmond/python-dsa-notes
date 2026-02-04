"""
Clone Graph Problem

Clean single-entry implementation surface.
"""

from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list['Node']] = None):
        self.val = val
        self.neighbors = neighbors or []


class Solution:
    def solve(self, node: Optional[Node]) -> Optional[Node]:
        """
        Implement the Clone Graph solution here.

        Args:
            node: Optional[Node]

        Returns:
            Optional[Node]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(node)


if __name__ == "__main__":
    pass
