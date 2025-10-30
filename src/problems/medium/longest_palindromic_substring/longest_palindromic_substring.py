"""
Longest Palindromic Substring Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, s: str) -> str:
        """
        Implement the Longest Palindromic Substring solution here.

        Args:
            s: str

        Returns:
            str
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def longest_palindromic_substring(s: str) -> str:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(s)


if __name__ == "__main__":
    pass
