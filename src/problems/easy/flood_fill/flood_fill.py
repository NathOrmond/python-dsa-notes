"""
Flood Fill Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Implement the Flood Fill solution here.

        Args:
            image: List[List[int]]
            sr: int
            sc: int
            newColor: int

        Returns:
            List[List[int]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def flood_fill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(image, sr, sc, newColor)


if __name__ == "__main__":
    pass
