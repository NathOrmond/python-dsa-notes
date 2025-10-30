"""
Letter Combinations Of A Phone Number Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, digits: str) -> List[str]:
        """
        Implement the Letter Combinations of a Phone Number solution here.

        Args:
            digits: str

        Returns:
            List[str]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def letter_combinations_of_a_phone_number(digits: str) -> List[str]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(digits)


if __name__ == "__main__":
    pass
