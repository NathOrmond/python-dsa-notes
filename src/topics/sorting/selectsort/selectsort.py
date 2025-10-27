"""
Selection Sort Implementation

This module contains selection sort implementation with method stub for practice.
"""

from math import inf
from typing import List


class Solution:
    """Solution class for selection sort."""
    
    def select_sort(self, nums: List[int]) -> List[int]:
        """
        Selection sort implementation.
        
        - Iterate through the list
        - Find the minimum element in the unsorted part
        - Swap it with the first element of the unsorted part
        - Repeat until the entire list is sorted
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)  # In-place sorting, only uses a few variables
        
        Args:
            nums: List of integers to sort
            
        Returns:
            List[int]: Sorted list of integers
        """
        # Implement selection sort
        # Hint: Find the minimum element and place it at the beginning
        # Hint: Repeat for remaining unsorted portion
        
        # Approach: Use separate variables to track minimum
        # min_val = value of smallest element found so far
        # min_index = position of smallest element
        for i in range(len(nums)):
            # Track minimum value and its index in the unsorted portion
            min_val = nums[i]
            min_index = i
            # Look through the rest of the array
            for j in range(i + 1, len(nums)):
                # Update min_val and min_index if you find a smaller element
                if nums[j] < min_val:
                    min_val = nums[j]
                    min_index = j 
            # Swap the minimum element with the element at position i
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums 



# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [64, 25, 12, 22, 11],
        [5, 2, 8, 1, 9],
        [1],
        [5, 1, 4, 2, 8]
    ]
    
    for nums in test_cases:
        result = solution.select_sort(nums.copy())
        print(f"Input: {nums}")
        print(f"Output: {result}")
        print()
