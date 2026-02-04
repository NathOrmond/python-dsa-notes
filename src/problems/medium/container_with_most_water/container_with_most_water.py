"""
Container With Most Water Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, height: List[int]) -> int:
        """
        Implement the Container With Most Water solution here.

        Args:
            height: List[int]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def container_with_most_water(height: List[int]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(height)


if __name__ == "__main__":
    pass
