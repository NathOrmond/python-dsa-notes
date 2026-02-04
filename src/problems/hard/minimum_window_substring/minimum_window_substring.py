"""
Minimum Window Substring Problem

Clean single-entry implementation surface.
"""

class Solution:
    def solve(self, s: str) -> int:
        """
        Implement the Minimum Window Substring solution here.

        Args:
            s: str

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def minimum_window_substring(s: str) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(s)


if __name__ == "__main__":
    pass
