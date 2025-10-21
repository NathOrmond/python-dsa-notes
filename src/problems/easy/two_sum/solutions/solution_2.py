"""
Two Sum - Hash Map Solution

This is the optimized approach using a hash map (dictionary) to store
complements as we iterate through the array.

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(n) - Hash map can store up to n elements
"""

from typing import List


def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    """
    Hash map approach: use dictionary to store complements.
    
    TODO: Implement this function
    - Use a dictionary to store numbers you've seen and their indices
    - For each number, calculate what complement you need to reach the target
    - Check if you've seen the complement before
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers that sum to target
    """
    # TODO: Implement hash map solution
    # Hint: Create an empty dictionary to store {value: index} pairs
    # Hint: For each number, calculate complement = target - num
    # Hint: If complement is in dictionary, return [dict[complement], current_index]
    # Hint: Otherwise, store current number and its index in the dictionary
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
        result = two_sum_hash_map(nums, target)
        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Correct: {result == expected}")
        print("-" * 40)
