"""
Two Sum Problem

This module contains the main solution interface and method stubs for different approaches.
"""

from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary of { complement, index } pairs
        complements = dict()
        for index, value in enumerate(nums):
            complement = target - value
            if( complement in complements ):
                return [ complements[complement], index ]
            else: 
                # We store each value we hit as a candidate 
                # complement for a future val 
                complements[value] = index; 
        return None


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Main function for two sum problem using hash map approach.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices that sum to target
    """
    complements = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in complements:
            return [complements[complement], index]
        complements[value] = index
    return []


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach for two sum.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices that sum to target
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input nums: {nums}, target: {target}")
    print(f"Output indices: {result}")
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Input nums: {nums2}, target: {target2}")
    print(f"Output indices: {result2}")
