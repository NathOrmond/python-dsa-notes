"""
Minimum Height Trees Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Implement the Minimum Height Trees solution here.

        Args:
            n: int
            edges: List[List[int]]

        Returns:
            List[int]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def minimum_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(n, edges)


if __name__ == "__main__":
    pass
