"""
Binary Search Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int], target: int) -> int:
        """
        Implement the Binary Search solution here.

        Args:
            nums: List[int]
            target: int

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def binary_search(nums: List[int], target: int) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums, target)


if __name__ == "__main__":
    pass
