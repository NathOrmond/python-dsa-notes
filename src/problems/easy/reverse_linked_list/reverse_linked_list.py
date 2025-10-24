"""
Reverse Linked List Problem

This module contains the solution for reversing a singly linked list.
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


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list.
    
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    
    Args:
        head: Head of the singly linked list
        
    Returns:
        Head of the reversed linked list
        
    Examples:
        >>> # Example 1: head = [1,2,3,4,5]
        >>> # Output: [5,4,3,2,1]
        >>> 
        >>> # Example 2: head = [1,2]
        >>> # Output: [2,1]
        >>> 
        >>> # Example 3: head = []
        >>> # Output: []
    """
    # TODO: Implement your solution here
    # Hint: Use three pointers: prev, current, and next
    # Hint: Iterate through the list and reverse the links
    # Hint: Return the new head (which was the original tail)
    pass


# Example usage
if __name__ == "__main__":
    # Test cases from the problem description
    print("Testing reverse_linked_list function:")
    
    # Example 1: head = [1,2,3,4,5]
    # Expected output: [5,4,3,2,1]
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result1 = reverse_linked_list(head1)
    print(f"Example 1: {result1}")
    
    # Example 2: head = [1,2]
    # Expected output: [2,1]
    head2 = ListNode(1, ListNode(2))
    result2 = reverse_linked_list(head2)
    print(f"Example 2: {result2}")
    
    # Example 3: head = []
    # Expected output: []
    result3 = reverse_linked_list(None)
    print(f"Example 3: {result3}")