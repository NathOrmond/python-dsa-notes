"""
Rotting Oranges Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, grid: List[List[int]]) -> int:
        """
        Implement the Rotting Oranges solution here.

        Args:
            grid: List[List[int]]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def rotting_oranges(grid: List[List[int]]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(grid)


if __name__ == "__main__":
    pass
