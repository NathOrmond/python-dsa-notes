"""
Binary Search Problem

Clean single-entry implementation surface.
"""

from typing import List


class Solution:
    def solve(self, nums: List[int], target: int) -> int:
        """
        Implement the Binary Search solution here.

        Args:
            nums: List[int]
            target: int

        Returns:
            int
        """
        return self.search(nums, target)

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = self.mid(low, high)
            curr = nums[mid]
            if curr == target:
                return mid
            if curr < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def mid(self, low: int, high: int):
        delta = (high - low) // 2
        return low + delta

if __name__ == "__main__":
    pass
