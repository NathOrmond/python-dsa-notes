"""
Insert Interval Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Implement the Insert Interval solution here.

        Args:
            intervals: List[List[int]]
            new_interval: List[int]

        Returns:
            List[List[int]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(intervals, new_interval)


if __name__ == "__main__":
    pass
