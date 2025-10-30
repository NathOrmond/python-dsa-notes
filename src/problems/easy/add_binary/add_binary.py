"""
Add Binary Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, a: str, b: str) -> str:
        """
        Implement the Add Binary solution here.

        Args:
            a: str
            b: str

        Returns:
            str
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def add_binary(a: str, b: str) -> str:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(a, b)


if __name__ == "__main__":
    pass
