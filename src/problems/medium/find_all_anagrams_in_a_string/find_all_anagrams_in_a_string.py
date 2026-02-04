"""
Find All Anagrams In A String Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, s: str, p: str):
        """
        Implement the Find All Anagrams in a String solution here.

        Args:
            s: str
            p: str

        Returns:
            Any (indices or boolean depending on desired format)
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def find_all_anagrams_in_a_string(s: str, p: str):
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(s, p)


if __name__ == "__main__":
    pass
