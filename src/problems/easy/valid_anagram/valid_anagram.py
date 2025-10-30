"""
Valid Anagram Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, s: str, t: str) -> bool:
        """
        Implement the Valid Anagram solution here.

        Args:
            s: str
            t: str

        Returns:
            bool
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def valid_anagram(s: str, t: str) -> bool:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(s, t)


if __name__ == "__main__":
    pass
