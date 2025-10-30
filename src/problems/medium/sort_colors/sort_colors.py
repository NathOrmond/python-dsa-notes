"""
Sort Colors Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> None:
        """
        Implement the Sort Colors solution here (in-place sort of 0,1,2).

        Args:
            nums: List[int]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def sort_colors(nums: List[int]) -> None:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums)


if __name__ == "__main__":
    pass
