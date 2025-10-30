"""
Number Of Islands Problem

Clean single-entry implementation surface.
"""

from typing import List, List as _List


class Solution:
    def solve(self, grid: _List[_List[str]]) -> int:
        """
        Implement the Number of Islands solution here.

        Args:
            grid: List[List[str]]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def number_of_islands(grid: List[List[str]]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(grid) 


if __name__ == "__main__":
    pass
