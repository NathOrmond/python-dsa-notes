"""
Task Scheduler Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, tasks: List[str], n: int) -> int:
        """
        Implement the Task Scheduler solution here.

        Args:
            tasks: List[str]
            n: int

        Returns:
            int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def task_scheduler(tasks: List[str], n: int) -> int:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(tasks, n)


if __name__ == "__main__":
    pass
