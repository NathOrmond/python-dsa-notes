"""
Evaluate Reverse Polish Notation Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, tokens: List[str]) -> int:
        """
        Implement the Evaluate Reverse Polish Notation solution here.

        Args:
            tokens: List[str]

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def evaluate_reverse_polish_notation(tokens: List[str]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(tokens)


if __name__ == "__main__":
    pass
