"""
Detect Cycle in Linked List Problem

This module contains the solution for detecting cycles in a linked list.
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """String representation for debugging."""
        values = []
        current = self
        visited = set()
        while current and current not in visited:
            visited.add(current)
            values.append(str(current.val))
            current = current.next
        if current:
            values.append("...")  # Indicates cycle
        return " -> ".join(values) + " -> None"


def detect_cycle_in_linked_list(head: Optional[ListNode]) -> bool:
    """
    Detect if there is a cycle in the linked list.
    
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached 
    again by continuously following the next pointer.
    
    Args:
        head: Head of the linked list
        
    Returns:
        True if there is a cycle in the linked list, False otherwise
        
    Examples:
        >>> # Example 1: head = [3,2,0,-4], pos = 1
        >>> # Output: true (cycle exists)
        >>> 
        >>> # Example 2: head = [1,2], pos = 0
        >>> # Output: true (cycle exists)
        >>> 
        >>> # Example 3: head = [1], pos = -1
        >>> # Output: false (no cycle)
    """
    # TODO: Implement your solution here
    # Hint: Use Floyd's cycle detection algorithm (tortoise and hare)
    # Hint: Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
    # Hint: If there's a cycle, fast will eventually catch up to slow
    # Hint: If fast reaches None, there's no cycle
    pass


# Example usage
if __name__ == "__main__":
    # Test cases from the problem description
    print("Testing detect_cycle_in_linked_list function:")
    
    # Example 1: head = [3,2,0,-4], pos = 1 (cycle exists)
    # Create nodes
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    # Link nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create cycle: -4 -> 2
    
    result1 = detect_cycle_in_linked_list(node1)
    print(f"Example 1: {result1}")  # Expected: True
    
    # Example 2: head = [1,2], pos = 0 (cycle exists)
    node5 = ListNode(1)
    node6 = ListNode(2)
    node5.next = node6
    node6.next = node5  # Create cycle: 2 -> 1
    
    result2 = detect_cycle_in_linked_list(node5)
    print(f"Example 2: {result2}")  # Expected: True
    
    # Example 3: head = [1], pos = -1 (no cycle)
    node7 = ListNode(1)
    result3 = detect_cycle_in_linked_list(node7)
    print(f"Example 3: {result3}")  # Expected: False
