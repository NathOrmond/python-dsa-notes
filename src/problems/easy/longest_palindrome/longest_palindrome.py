"""
Longest Palindrome Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, s: str) -> bool:
        """
        Implement the Longest Palindrome solution here.

        Args:
            s: str

        Returns:
            bool
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def longest_palindrome(s: str) -> bool:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(s)


if __name__ == "__main__":
    pass
