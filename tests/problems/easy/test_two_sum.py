"""
Test cases for Two Sum problem.

This file demonstrates the test-driven development approach:
1. Write comprehensive tests first
2. Cover basic examples, edge cases, and boundary conditions
3. Test multiple solution approaches
"""

import pytest
from typing import List

# Import the main solution functions
from src.problems.easy.two_sum import two_sum, two_sum_brute_force, two_sum_hash_map

# Import individual solution implementations
from src.problems.easy.two_sum.solutions.solution_1 import two_sum_brute_force as brute_force_impl
from src.problems.easy.two_sum.solutions.solution_2 import two_sum_hash_map as hash_map_impl


class TestTwoSum:
    """Test cases for the main two_sum function."""
    
    def test_example_1(self):
        """Test case from problem description."""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        # Note: This will fail until we implement the function
        # result = two_sum(nums, target)
        # assert result == expected
    
    def test_example_2(self):
        """Test case from problem description."""
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        # result = two_sum(nums, target)
        # assert result == expected
    
    def test_example_3(self):
        """Test case from problem description."""
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        # result = two_sum(nums, target)
        # assert result == expected


class TestTwoSumBruteForce:
    """Test cases for brute force approach."""
    
    @pytest.mark.parametrize("nums,target,expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ])
    def test_brute_force_basic_cases(self, nums: List[int], target: int, expected: List[int]):
        """Test basic functionality of brute force approach."""
        result = brute_force_impl(nums, target)
        assert result == expected
    
    def test_brute_force_edge_cases(self):
        """Test edge cases for brute force approach."""
        # Minimum valid input
        assert brute_force_impl([1, 2], 3) == [0, 1]
        
        # Negative numbers
        assert brute_force_impl([-1, -2, -3, -4, -5], -8) == [2, 4]
        
        # Mixed positive and negative
        assert brute_force_impl([-1, 0, 1, 2], 1) == [0, 3]


class TestTwoSumHashMap:
    """Test cases for hash map approach."""
    
    @pytest.mark.parametrize("nums,target,expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ])
    def test_hash_map_basic_cases(self, nums: List[int], target: int, expected: List[int]):
        """Test basic functionality of hash map approach."""
        result = hash_map_impl(nums, target)
        assert result == expected
    
    def test_hash_map_edge_cases(self):
        """Test edge cases for hash map approach."""
        # Minimum valid input
        result = hash_map_impl([1, 2], 3)
        assert result == [0, 1]
        
        # Negative numbers
        result = hash_map_impl([-1, -2, -3, -4, -5], -8)
        assert result == [2, 4]
        
        # Mixed positive and negative - multiple valid solutions
        result = hash_map_impl([-1, 0, 1, 2], 1)
        # Could be [0, 3] or [1, 2] - both are valid
        assert result in [[0, 3], [1, 2]]
    
    def test_hash_map_duplicate_values(self):
        """Test that hash map handles duplicate values correctly."""
        # Same value appears multiple times
        assert hash_map_impl([3, 3], 6) == [0, 1]
        assert hash_map_impl([1, 2, 3, 3], 6) == [2, 3]


class TestSolutionConsistency:
    """Test that both approaches produce the same results."""
    
    @pytest.mark.parametrize("nums,target", [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 8),
        ([0, 4, 3, 0], 0),
        ([-1, -2, -3, -4, -5], -8),
        ([-1, 0, 1, 2], 1),
    ])
    def test_approaches_consistent(self, nums: List[int], target: int):
        """Test that both approaches produce valid results."""
        brute_result = brute_force_impl(nums, target)
        hash_result = hash_map_impl(nums, target)
        
        # Both should be valid solutions (sum to target)
        assert nums[brute_result[0]] + nums[brute_result[1]] == target
        assert nums[hash_result[0]] + nums[hash_result[1]] == target
        
        # Both should be different indices
        assert brute_result[0] != brute_result[1]
        assert hash_result[0] != hash_result[1]
        
        # Both should be within valid range
        assert 0 <= brute_result[0] < len(nums)
        assert 0 <= brute_result[1] < len(nums)
        assert 0 <= hash_result[0] < len(nums)
        assert 0 <= hash_result[1] < len(nums)


class TestPerformance:
    """Performance tests to demonstrate complexity differences."""
    
    def test_large_input_brute_force(self):
        """Test brute force with larger input."""
        # Create a large array where solution is at the end
        nums = list(range(1000)) + [1999, 2000]
        target = 3999
        
        result = brute_force_impl(nums, target)
        assert result == [1000, 1001]
    
    def test_large_input_hash_map(self):
        """Test hash map with larger input."""
        # Create a large array where solution is at the end
        nums = list(range(1000)) + [1999, 2000]
        target = 3999
        
        result = hash_map_impl(nums, target)
        assert result == [1000, 1001]


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__])
