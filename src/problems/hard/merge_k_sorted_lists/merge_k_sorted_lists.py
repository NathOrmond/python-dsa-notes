"""
Merge K Sorted Lists Problem

Clean single-entry implementation surface.
"""

from typing import List, Optional, Any


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Implement the Merge K Sorted Lists solution here.

        Args:
            lists: List[Optional[ListNode]]

        Returns:
            Optional[ListNode]
        """
        raise NotImplementedError("Implement the single canonical solution in Solution.solve")


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(lists)


if __name__ == "__main__":
    pass
