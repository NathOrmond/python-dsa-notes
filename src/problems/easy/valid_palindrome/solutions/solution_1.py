"""
Solution for Valid Palindrome
"""

from typing import List, Optional


def valid_palindrome_clean_and_compare(s: str) -> bool:
    """
    Clean and compare approach for valid palindrome.
    
    Args:
        s: String to check
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    clean_text = ''.join(char for char in s.lower() if char.isalnum())
    for index, char in enumerate(clean_text):
        if char != clean_text[len(clean_text) - index - 1]:
            return False
    return True


# Example usage
if __name__ == "__main__":
    print(f"valid_palindrome_clean_and_compare('A man, a plan, a canal: Panama') = {valid_palindrome_clean_and_compare('A man, a plan, a canal: Panama')}")
    print(f"valid_palindrome_clean_and_compare('race a car') = {valid_palindrome_clean_and_compare('race a car')}")
    print(f"valid_palindrome_clean_and_compare(' ') = {valid_palindrome_clean_and_compare(' ')}")
