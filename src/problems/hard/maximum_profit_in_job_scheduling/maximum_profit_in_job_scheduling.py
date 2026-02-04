"""
Maximum Profit In Job Scheduling Problem

Clean single-entry implementation surface.
"""

from typing import List, Tuple


class Solution:
    def solve(self, jobs: List[Tuple[int, int, int]]) -> int:
        """
        Implement the Maximum Profit in Job Scheduling solution here.

        Args:
            jobs: List of (start, end, profit)

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def maximum_profit_in_job_scheduling(jobs: List[Tuple[int, int, int]]) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(jobs)


if __name__ == "__main__":
    pass
