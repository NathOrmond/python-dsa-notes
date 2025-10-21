"""
Two Sum - Brute Force Solution

This is the most straightforward approach: check every pair of numbers
to see if they sum to the target.

Time Complexity: O(n²) - We check every pair
Space Complexity: O(1) - Only using a constant amount of extra space
"""

from typing import List


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach: check all pairs.
    
    TODO: Implement this function
    - Use nested loops to check every pair of numbers
    - Return the indices of the two numbers that sum to target
    - Time Complexity: O(n²)
    - Space Complexity: O(1)
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers that sum to target
    """
    # TODO: Implement brute force solution
    # Hint: Use nested loops - outer loop for first number, inner loop for second number
    # Hint: Make sure j > i to avoid checking the same pair twice
    pass


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for nums, target, expected in test_cases:
        result = two_sum_brute_force(nums, target)
        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Correct: {result == expected}")
        print("-" * 40)
