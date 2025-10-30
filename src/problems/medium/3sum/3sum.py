"""
3Sum Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> List[List[int]]:
        """
        Implement the 3Sum solution here.

        Args:
            nums: List[int]

        Returns:
            List[List[int]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def three_sum(nums: List[int]) -> List[List[int]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums)


if __name__ == "__main__":
    pass
