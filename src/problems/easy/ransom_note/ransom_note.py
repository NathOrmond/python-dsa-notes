"""
Ransom Note Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, ransom: str, magazine: str) -> bool:
        """
        Implement the Ransom Note solution here.

        Args:
            ransom: str
            magazine: str

        Returns:
            bool
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def ransom_note(ransom: str, magazine: str) -> bool:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(ransom, magazine)


if __name__ == "__main__":
    pass
