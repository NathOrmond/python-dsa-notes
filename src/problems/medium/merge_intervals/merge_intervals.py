"""
Merge Intervals Problem

Clean single-entry implementation surface.
"""

from typing import List, List as _List


class Solution:
    def solve(self, intervals: _List[_List[int]]) -> _List[_List[int]]:
        """
        Implement the Merge Intervals solution here.

        Args:
            intervals: List[List[int]]

        Returns:
            List[List[int]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(intervals)


if __name__ == "__main__":
    pass
