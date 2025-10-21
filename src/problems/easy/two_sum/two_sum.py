"""
Two Sum Problem

Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

You can return the answer in any order.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in nums that add up to target.
    
    This is the main interface function that uses the optimal hash map approach.
    For learning purposes, see solutions/ directory for different implementations.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers that sum to target
        
    Raises:
        ValueError: If no solution exists (should not happen per problem constraints)
    """
    # Use the hash map solution as the main implementation
    return two_sum_hash_map(nums, target)


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach: check all pairs.
    
    TODO: Implement this function
    - Use nested loops to check every pair of numbers
    - Return the indices of the two numbers that sum to target
    - Time Complexity: O(n²)
    - Space Complexity: O(1)
    """
    # TODO: Implement brute force solution
    # Hint: Use nested loops - outer loop for first number, inner loop for second number
    # Hint: Make sure j > i to avoid checking the same pair twice
    pass


def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    """
    Hash map approach: use dictionary to store complements.
    
    TODO: Implement this function
    - Use a dictionary to store numbers you've seen and their indices
    - For each number, calculate what complement you need to reach the target
    - Check if you've seen the complement before
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    """
    # TODO: Implement hash map solution
    # Hint: Create an empty dictionary to store {value: index} pairs
    # Hint: For each number, calculate complement = target - num
    # Hint: If complement is in dictionary, return [dict[complement], current_index]
    # Hint: Otherwise, store current number and its index in the dictionary
    pass