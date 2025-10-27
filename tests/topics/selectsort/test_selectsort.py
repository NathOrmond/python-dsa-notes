"""
Tests for Selection Sort
"""

import pytest
from typing import List
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from topics.sorting.selectsort.selectsort import Solution


class TestSelectionSort:
    """Test cases for selection sort implementations."""
    
    def test_basic_sort(self):
        """Test basic sorting of unsorted array."""
        nums = [64, 25, 12, 22, 11]
        solution = Solution()
        result = solution.select_sort(nums.copy())
        expected = sorted(nums)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_sorted_array(self):
        """Test with already sorted array."""
        nums = [1, 2, 3, 4, 5]
        solution = Solution()
        result = solution.select_sort(nums.copy())
        assert result == nums, f"Sorted array should remain the same"
    
    def test_reverse_sorted_array(self):
        """Test with reverse sorted array."""
        nums = [5, 4, 3, 2, 1]
        solution = Solution()
        result = solution.select_sort(nums.copy())
        expected = sorted(nums)
        assert result == expected
    
    def test_single_element(self):
        """Test with single element array."""
        nums = [42]
        solution = Solution()
        result = solution.select_sort(nums.copy())
        assert result == nums
    
    def test_empty_array(self):
        """Test with empty array."""
        nums = []
        solution = Solution()
        result = solution.select_sort(nums.copy())
        assert result == nums
    
    def test_duplicate_values(self):
        """Test with duplicate values."""
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        solution = Solution()
        result = solution.select_sort(nums.copy())
        expected = sorted(nums)
        assert result == expected
    
    def test_negative_values(self):
        """Test with negative values."""
        nums = [-5, -2, -8, 3, 1, -1]
        solution = Solution()
        result = solution.select_sort(nums.copy())
        expected = sorted(nums)
        assert result == expected
    
    def test_large_array(self):
        """Test with larger array."""
        nums = list(range(50, 0, -1))
        solution = Solution()
        result = solution.select_sort(nums.copy())
        expected = sorted(nums)
        assert result == expected
    
    def test_all_same_values(self):
        """Test with all elements being the same."""
        nums = [5, 5, 5, 5, 5]
        solution = Solution()
        result = solution.select_sort(nums.copy())
        assert result == nums
    
    def test_two_elements(self):
        """Test with exactly two elements."""
        test_cases = [[1, 2], [2, 1], [3, 3]]
        solution = Solution()
        for nums in test_cases:
            result = solution.select_sort(nums.copy())
            expected = sorted(nums)
            assert result == expected


    def test_performance_medium_array(self):
        """Test performance with medium-sized array."""
        nums = list(range(50, 0, -1))
        solution = Solution()
        result = solution.select_sort(nums.copy())
        expected = sorted(nums)
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

