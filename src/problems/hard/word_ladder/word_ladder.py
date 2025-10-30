"""
Word Ladder Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        """
        Implement the Word Ladder solution here.

        Args:
            nums: List[int]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def word_ladder(nums: List[int]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(nums)


if __name__ == "__main__":
    pass
