"""
Word Search Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        """
        Implement the Word Search solution here.

        Args:
            nums: List[int]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def word_search(nums: List[int]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums)


if __name__ == "__main__":
    pass
