"""
Valid Palindrome Problem

This module contains the main solution interface and method stubs for different approaches.
"""

from typing import List, Optional

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(char for char in s.lower() if char.isalnum())
        for index, char in enumerate(clean_text):
            if char != clean_text[len(clean_text) - index - 1]:
                return False
        return True


def valid_palindrome(s: str) -> bool:
    """
    Main function for valid palindrome problem.
    
    Args:
        s: String to check
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    solution = Solution()
    return solution.isPalindrome(s)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Input: {s1}")
    print(f"Output: {solution.isPalindrome(s1)}")
    
    # Example 2
    s2 = "race a car"
    print(f"\nInput: {s2}")
    print(f"Output: {solution.isPalindrome(s2)}")
    
    # Example 3
    s3 = " "
    print(f"\nInput: '{s3}'")
    print(f"Output: {solution.isPalindrome(s3)}")
