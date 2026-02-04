"""
Largest Rectangle In Histogram Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, heights: List[int]) -> int:
        """
        Implement the Largest Rectangle in Histogram solution here.

        Args:
            heights: List[int]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def largest_rectangle_in_histogram(heights: List[int]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(heights)


if __name__ == "__main__":
    pass
