"""
Quick Sort Implementation

This module contains quicksort implementation with method stub for practice.
"""

from typing import List
import random


class Solution:
    """Solution class for quicksort."""
    
    def quick_sort(self, nums: List[int]) -> List[int]:
        """
        Quicksort implementation.

        - Choose a pivot (commonly first, last, or middle element)
        - Partition the array around the pivot
        - Recursively sort left and right sub-arrays
        
        Time Complexity: O(n log n) average, O(n^2) worst case
        Space Complexity: O(n)  # Creates new lists, not in-place
        
        Args:
            nums: List of integers to sort
            
        Returns:
            List[int]: Sorted list of integers
        """

        if len(nums) < 2:
            return nums
        
        # Choose pivot (random index between 0 and len-1)
        pivot_idx = random.randint(0, len(nums) - 1)
        pivot = nums[pivot_idx]
        
        smaller = []
        greater = []
        
        # Partition elements around pivot
        for i in range(len(nums)):
            if i == pivot_idx:  # Skip the pivot element itself
                continue
            if nums[i] < pivot:
                smaller.append(nums[i])
            else:
                greater.append(nums[i])
        
        # Recursively sort and combine
        return self.quick_sort(smaller) + [pivot] + self.quick_sort(greater)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [64, 25, 12, 22, 11],
        [5, 2, 8, 1, 9],
        [1],
        [5, 1, 4, 2, 8],
        [10, 7, 8, 9, 1, 5]
    ]
    
    for nums in test_cases:
        result = solution.quick_sort(nums.copy())
        print(f"Input: {nums}")
        print(f"Output: {result}")
        print()

