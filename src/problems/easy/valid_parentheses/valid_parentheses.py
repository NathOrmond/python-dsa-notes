"""
Valid Parentheses Problem

This module contains the main solution interface and method stubs for different approaches.
"""

from typing import List, Optional


def valid_parentheses(s: str) -> bool:
    """
    Determines if the input string containing parentheses is valid.
    Valid means: open brackets are closed by the same type, in correct order,
    and every close bracket has a corresponding open bracket.
    
    Args:
        s: String containing only '(', ')', '{', '}', '[' and ']'
        
    Returns:
        bool: True if the string is valid, False otherwise
    """
    # We are going to initialise a stack to keep track of parentheses as we go
    # When we encounter an open parenthesis we will add it to the stack
    # When we encounter a closing parenthesis we will pop the stacka and check 
    # for a match
    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if len(stack) == 0:
                return False;
            else:
                curr = stack.pop()
                if brackets[curr] != char:
                    return False;
        else:
            continue;
    return len(stack) == 0;



# Example usage
if __name__ == "__main__":
    # Test cases from the problem description
    test_cases = [
        "()",      # True
        "()[]{}",  # True  
        "(]",      # False
        "([])",    # True
        "([)]",    # False
    ]
    
    print("Testing valid_parentheses function:")
    for test_case in test_cases:
        result = valid_parentheses(test_case)
        print(f"valid_parentheses('{test_case}') = {result}")
