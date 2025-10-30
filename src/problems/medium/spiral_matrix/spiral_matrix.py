"""
Spiral Matrix Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, matrix: List[List[int]]) -> List[int]:
        """
        Implement the Spiral Matrix solution here.

        Args:
            matrix: List[List[int]]

        Returns:
            List[int]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(matrix)


if __name__ == "__main__":
    pass
