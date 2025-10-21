"""
Valid Parentheses - Stack Solution

TODO: Add description of stack approach

Time Complexity: O(n) - Single pass through the string
Space Complexity: O(n) - Stack can store up to n/2 elements
"""

from typing import List


def valid_parentheses_stack(s: str) -> bool:
    """
    Stack-based approach.
    
    TODO: Implement this function
    - Add implementation hints here
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    Args:
        s: Input string containing parentheses
        
    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement stack solution
    # Hint: Use a stack to keep track of opening brackets
    # Hint: When you see a closing bracket, check if it matches the top of stack
    # Hint: Create a mapping of closing to opening brackets: {')': '(', '}': '{', ']': '['}
    # Hint: If stack is empty when you see a closing bracket, it's invalid
    # Hint: If stack is not empty at the end, it's invalid
    pass


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    
    for test_input, expected in test_cases:
        result = valid_parentheses_stack(test_input)
        print(f"Input: {test_input}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Correct: {result == expected}")
        print("-" * 40)
