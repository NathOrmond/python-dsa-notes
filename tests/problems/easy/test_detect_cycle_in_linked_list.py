"""
Tests for Detect Cycle in Linked List
"""

import pytest
from src.problems.easy.detect_cycle_in_linked_list.detect_cycle_in_linked_list import detect_cycle_in_linked_list, ListNode


class TestDetectCycleInLinkedList:
    """Test cases for detect_cycle_in_linked_list problem."""
    
    def test_basic_examples(self):
        """Test basic examples from problem description."""
        # Example 1: head = [3,2,0,-4], pos = 1 (cycle exists)
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Create cycle: -4 -> 2
        
        assert detect_cycle_in_linked_list(node1) == True
    
    def test_two_node_cycle(self):
        """Test with two nodes forming a cycle."""
        # Example 2: head = [1,2], pos = 0 (cycle exists)
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1  # Create cycle: 2 -> 1
        
        assert detect_cycle_in_linked_list(node1) == True
    
    def test_no_cycle(self):
        """Test with no cycle."""
        # Example 3: head = [1], pos = -1 (no cycle)
        node1 = ListNode(1)
        assert detect_cycle_in_linked_list(node1) == False
        
        # Test with multiple nodes but no cycle
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        assert detect_cycle_in_linked_list(node1) == False
    
    def test_empty_list(self):
        """Test with empty list."""
        assert detect_cycle_in_linked_list(None) == False
    
    def test_single_node_no_cycle(self):
        """Test single node with no cycle."""
        node = ListNode(42)
        assert detect_cycle_in_linked_list(node) == False
    
    def test_single_node_self_cycle(self):
        """Test single node pointing to itself."""
        node = ListNode(42)
        node.next = node  # Self cycle
        assert detect_cycle_in_linked_list(node) == True
    
    def test_large_cycle(self):
        """Test with larger cycle."""
        # Create a list with 10 nodes forming a cycle
        nodes = [ListNode(i) for i in range(10)]
        
        # Link nodes linearly
        for i in range(9):
            nodes[i].next = nodes[i + 1]
        
        # Create cycle: last node points to first
        nodes[9].next = nodes[0]
        
        assert detect_cycle_in_linked_list(nodes[0]) == True
    
    def test_cycle_at_end(self):
        """Test cycle starting from the last node."""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node3  # Cycle: 4 -> 3
        
        assert detect_cycle_in_linked_list(node1) == True
    
    def test_cycle_in_middle(self):
        """Test cycle starting from middle node."""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node2  # Cycle: 5 -> 2
        
        assert detect_cycle_in_linked_list(node1) == True
    
    def test_negative_values(self):
        """Test with negative values."""
        node1 = ListNode(-1)
        node2 = ListNode(-2)
        node3 = ListNode(-3)
        
        node1.next = node2
        node2.next = node3
        node3.next = node1  # Cycle: -3 -> -1
        
        assert detect_cycle_in_linked_list(node1) == True
    
    def test_boundary_values(self):
        """Test with boundary values from constraints."""
        # Test with maximum constraint values
        node1 = ListNode(-100000)
        node2 = ListNode(100000)
        
        node1.next = node2
        node2.next = node1  # Cycle
        
        assert detect_cycle_in_linked_list(node1) == True
    
    def test_long_list_no_cycle(self):
        """Test with long list but no cycle."""
        # Create a list with 1000 nodes (within constraint)
        head = ListNode(0)
        current = head
        for i in range(1, 1000):
            current.next = ListNode(i)
            current = current.next
        
        assert detect_cycle_in_linked_list(head) == False
    
    def test_duplicate_values_with_cycle(self):
        """Test with duplicate values and cycle."""
        node1 = ListNode(1)
        node2 = ListNode(1)
        node3 = ListNode(2)
        node4 = ListNode(2)
        
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Cycle: 2 -> 1
        
        assert detect_cycle_in_linked_list(node1) == True
    
    def test_cycle_detection_performance(self):
        """Test performance with large cycle."""
        # Create a large cycle (within constraints)
        nodes = [ListNode(i) for i in range(1000)]
        
        # Link nodes linearly
        for i in range(999):
            nodes[i].next = nodes[i + 1]
        
        # Create cycle: last node points to middle node
        nodes[999].next = nodes[500]
        
        assert detect_cycle_in_linked_list(nodes[0]) == True


if __name__ == "__main__":
    pytest.main([__file__])
