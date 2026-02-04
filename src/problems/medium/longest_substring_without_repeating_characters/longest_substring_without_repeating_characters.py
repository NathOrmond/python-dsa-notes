"""
Longest Substring Without Repeating Characters Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, s: str) -> int:
        """
        Implement the Longest Substring Without Repeating Characters solution here.

        Args:
            s: str

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def longest_substring_without_repeating_characters(s: str) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(s)


if __name__ == "__main__":
    pass
