"""
Product Of Array Except Self Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        """
        Implement the Product of Array Except Self solution here.

        Args:
            nums: List[int]

        Returns:
            List[int]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def product_of_array_except_self(nums: List[int]) -> List[int]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums)


if __name__ == "__main__":
    pass
