"""
01 Matrix Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Implement the 01 Matrix solution here.

        Args:
            mat: List[List[int]]

        Returns:
            List[List[int]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def matrix_01(mat: List[List[int]]) -> List[List[int]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(mat)


if __name__ == "__main__":
    pass
