"""
Trapping Rain Water Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, height: List[int]) -> int:
        """
        Implement the Trapping Rain Water solution here.

        Args:
            height: List[int]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def trapping_rain_water(height: List[int]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(height)


if __name__ == "__main__":
    pass
