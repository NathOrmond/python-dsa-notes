"""
Tests for Reverse Linked List
"""

import pytest
from src.problems.easy.reverse_linked_list.reverse_linked_list import reverse_linked_list, ListNode


class TestReverseLinkedList:
    """Test cases for reverse_linked_list problem."""
    
    def test_basic_examples(self):
        """Test basic examples from problem description."""
        # Example 1: head = [1,2,3,4,5]
        # Expected output: [5,4,3,2,1]
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = reverse_linked_list(head)
        
        expected_values = [5, 4, 3, 2, 1]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_two_nodes(self):
        """Test with two nodes."""
        # Example 2: head = [1,2]
        # Expected output: [2,1]
        head = ListNode(1, ListNode(2))
        result = reverse_linked_list(head)
        
        assert result is not None
        assert result.val == 2
        assert result.next is not None
        assert result.next.val == 1
        assert result.next.next is None
    
    def test_empty_list(self):
        """Test with empty list."""
        # Example 3: head = []
        # Expected output: []
        result = reverse_linked_list(None)
        assert result is None
    
    def test_single_node(self):
        """Test with single node."""
        head = ListNode(42)
        result = reverse_linked_list(head)
        
        assert result is not None
        assert result.val == 42
        assert result.next is None
    
    def test_negative_values(self):
        """Test with negative values."""
        head = ListNode(-1, ListNode(-2, ListNode(-3)))
        result = reverse_linked_list(head)
        
        expected_values = [-3, -2, -1]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_mixed_values(self):
        """Test with mixed positive and negative values."""
        head = ListNode(-5, ListNode(0, ListNode(5)))
        result = reverse_linked_list(head)
        
        expected_values = [5, 0, -5]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_boundary_values(self):
        """Test with boundary values from constraints."""
        # Test with maximum constraint values
        head = ListNode(-5000, ListNode(0, ListNode(5000)))
        result = reverse_linked_list(head)
        
        expected_values = [5000, 0, -5000]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_large_list(self):
        """Test with larger list (within constraints)."""
        # Create a list with 100 nodes
        head = None
        for i in range(100):
            head = ListNode(i, head)
        
        result = reverse_linked_list(head)
        
        # Verify reversed order
        current = result
        for i in range(100):
            assert current is not None
            assert current.val == i
            current = current.next
        assert current is None
    
    def test_duplicate_values(self):
        """Test with duplicate values."""
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))
        result = reverse_linked_list(head)
        
        expected_values = [2, 2, 1, 1]
        current = result
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None
    
    def test_reverse_twice(self):
        """Test that reversing twice returns original list."""
        original_head = ListNode(1, ListNode(2, ListNode(3)))
        
        # Reverse once
        reversed_head = reverse_linked_list(original_head)
        
        # Reverse again
        double_reversed = reverse_linked_list(reversed_head)
        
        # Should be back to original order
        expected_values = [1, 2, 3]
        current = double_reversed
        for expected_val in expected_values:
            assert current is not None
            assert current.val == expected_val
            current = current.next
        assert current is None


if __name__ == "__main__":
    pytest.main([__file__])