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
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(nums)
    
    # Check every pair of numbers
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    # This should never be reached given problem constraints
    raise ValueError("No solution found")


def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    """
    Hash map approach: use dictionary to store complements.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Dictionary to store {value: index} pairs
    num_to_index = {}
    
    for i, num in enumerate(nums):
        # Calculate what number we need to reach the target
        complement = target - num
        
        # If we've seen the complement before, we found our pair
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Store current number and its index for future lookups
        num_to_index[num] = i
    
    # This should never be reached given problem constraints
    raise ValueError("No solution found")