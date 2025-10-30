"""
Partition Equal Subset Sum Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        """
        Implement the Partition Equal Subset Sum solution here.

        Args:
            nums: List[int]

        Returns:
            bool
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def partition_equal_subset_sum(nums: List[int]) -> bool:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums)


if __name__ == "__main__":
    pass
