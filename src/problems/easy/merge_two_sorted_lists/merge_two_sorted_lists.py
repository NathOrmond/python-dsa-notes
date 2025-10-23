"""
Merge Two Sorted Lists Problem

This module contains the solution for merging two sorted linked lists.
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
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values) + " -> None"


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted list.
    
    The list should be made by splicing together the nodes of the first two lists.
    
    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
        
    Examples:
        >>> # Example 1: list1 = [1,2,4], list2 = [1,3,4]
        >>> # Output: [1,1,2,3,4,4]
        >>> 
        >>> # Example 2: list1 = [], list2 = []
        >>> # Output: []
        >>> 
        >>> # Example 3: list1 = [], list2 = [0]
        >>> # Output: [0]
    """
    # TODO: Implement your solution here
    # Hint: Use a dummy node to simplify the merging process
    # Hint: Compare values from both lists and link the smaller one
    # Hint: Handle remaining nodes from either list
    pass


# Example usage
if __name__ == "__main__":
    # Test cases from the problem description
    print("Testing merge_two_sorted_lists function:")
    
    # Example 1: list1 = [1,2,4], list2 = [1,3,4]
    # Expected output: [1,1,2,3,4,4]
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result1 = merge_two_sorted_lists(list1, list2)
    print(f"Example 1: {result1}")
    
    # Example 2: list1 = [], list2 = []
    # Expected output: []
    result2 = merge_two_sorted_lists(None, None)
    print(f"Example 2: {result2}")
    
    # Example 3: list1 = [], list2 = [0]
    # Expected output: [0]
    list3 = ListNode(0)
    result3 = merge_two_sorted_lists(None, list3)
    print(f"Example 3: {result3}")
