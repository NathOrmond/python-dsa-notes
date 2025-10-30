"""
Search In Rotated Sorted Array Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int], target: int) -> int:
        """
        Implement the Search in Rotated Sorted Array solution here.

        Args:
            nums: List[int]
            target: int

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums, target)


if __name__ == "__main__":
    pass
