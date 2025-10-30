"""
K Closest Points To Origin Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Implement the K Closest Points to Origin solution here.

        Args:
            points: List[List[int]]
            k: int

        Returns:
            List[List[int]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def k_closest_points_to_origin(points: List[List[int]], k: int) -> List[List[int]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(points, k)


if __name__ == "__main__":
    pass
