"""
Lru Cache Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, capacity: int):
        """
        Implement the LRU Cache solution here (class with get/put).

        Args:
            capacity: int
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def lru_cache(capacity: int):
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(capacity)


if __name__ == "__main__":
    pass
