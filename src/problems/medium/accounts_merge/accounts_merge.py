"""
Accounts Merge Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Implement the Accounts Merge solution here.

        Args:
            accounts: List[List[str]]

        Returns:
            List[List[str]]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(accounts)


if __name__ == "__main__":
    pass
