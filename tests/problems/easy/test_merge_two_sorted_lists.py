"""
Tests for Merge Two Sorted Lists
"""

import pytest
from src.problems.easy.merge_two_sorted_lists.merge_two_sorted_lists import merge_two_sorted_lists, ListNode


class TestMergeTwoSortedLists:
    """Test cases for merge_two_sorted_lists problem."""
    
    def test_basic_examples(self):
        """Test basic examples from problem description."""
        # Example 1: list1 = [1,2,4], list2 = [1,3,4]
        # Expected output: [1,1,2,3,4,4]
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        result = merge_two_sorted_lists(list1, list2)
        
        # Check the merged list structure
        expected_values = [1, 1, 2, 3, 4, 4]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None  # End of list
    
    def test_empty_lists(self):
        """Test with empty lists."""
        # Example 2: list1 = [], list2 = []
        # Expected output: []
        result = merge_two_sorted_lists(None, None)
        assert result is None
    
    def test_one_empty_list(self):
        """Test with one empty list."""
        # Example 3: list1 = [], list2 = [0]
        # Expected output: [0]
        list2 = ListNode(0)
        result = merge_two_sorted_lists(None, list2)
        
        assert result is not None
        assert result.val == 0
        assert result.next is None
        
        # Test the reverse case: list1 = [0], list2 = []
        list1 = ListNode(0)
        result2 = merge_two_sorted_lists(list1, None)
        
        assert result2 is not None
        assert result2.val == 0
        assert result2.next is None
    
    def test_single_node_lists(self):
        """Test with single node lists."""
        list1 = ListNode(1)
        list2 = ListNode(2)
        result = merge_two_sorted_lists(list1, list2)
        
        assert result is not None
        assert result.val == 1
        assert result.next is not None
        assert result.next.val == 2
        assert result.next.next is None
    
    def test_duplicate_values(self):
        """Test with duplicate values."""
        list1 = ListNode(1, ListNode(1, ListNode(2)))
        list2 = ListNode(1, ListNode(3))
        result = merge_two_sorted_lists(list1, list2)
        
        expected_values = [1, 1, 1, 2, 3]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_one_list_longer(self):
        """Test when one list is significantly longer."""
        list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        list2 = ListNode(6)
        result = merge_two_sorted_lists(list1, list2)
        
        expected_values = [1, 2, 3, 4, 5, 6]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_negative_values(self):
        """Test with negative values (within constraints)."""
        list1 = ListNode(-5, ListNode(-1, ListNode(0)))
        list2 = ListNode(-3, ListNode(2))
        result = merge_two_sorted_lists(list1, list2)
        
        expected_values = [-5, -3, -1, 0, 2]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_edge_case_boundary_values(self):
        """Test with boundary values from constraints."""
        # Test with minimum value (-100)
        list1 = ListNode(-100, ListNode(0))
        list2 = ListNode(-50, ListNode(100))
        result = merge_two_sorted_lists(list1, list2)
        
        expected_values = [-100, -50, 0, 100]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_identical_lists(self):
        """Test with identical lists."""
        list1 = ListNode(1, ListNode(2, ListNode(3)))
        list2 = ListNode(1, ListNode(2, ListNode(3)))
        result = merge_two_sorted_lists(list1, list2)
        
        expected_values = [1, 1, 2, 2, 3, 3]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_performance_large_lists(self):
        """Test performance with larger lists (within constraints)."""
        # Create two sorted lists with 25 nodes each (total 50, within constraint)
        list1_values = list(range(0, 50, 2))  # [0, 2, 4, ..., 48]
        list2_values = list(range(1, 50, 2))  # [1, 3, 5, ..., 49]
        
        # Build list1
        list1 = None
        for val in reversed(list1_values):
            list1 = ListNode(val, list1)
        
        # Build list2
        list2 = None
        for val in reversed(list2_values):
            list2 = ListNode(val, list2)
        
        result = merge_two_sorted_lists(list1, list2)
        
        # Verify merged list contains all values in sorted order
        expected_values = list(range(50))  # [0, 1, 2, ..., 49]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None


if __name__ == "__main__":
    pytest.main([__file__])