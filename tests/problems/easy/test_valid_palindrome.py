"""
Tests for Valid Palindrome
"""

import pytest
from src.problems.easy.valid_palindrome import valid_palindrome


class TestValidPalindrome:
    """Test cases for valid_palindrome problem."""
    
    def test_basic_examples(self):
        """Test with basic examples."""
        # Example 1: Classic palindrome
        assert valid_palindrome("A man, a plan, a canal: Panama") == True
        # Example 2: Not a palindrome
        assert valid_palindrome("race a car") == False
        # Example 3: Single space (empty after cleaning)
        assert valid_palindrome(" ") == True
        # Example 4: Simple palindrome
        assert valid_palindrome("racecar") == True
        # Example 5: Not a palindrome
        assert valid_palindrome("hello") == False
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Empty string
        assert valid_palindrome("") == True
        # Single character
        assert valid_palindrome("a") == True
        # Single alphanumeric character
        assert valid_palindrome("A") == True
        # Only special characters (empty after cleaning)
        assert valid_palindrome("@#$%^&*") == True
        # Palindrome with all special characters
        assert valid_palindrome("A, B, A") == True
        # Palindrome with numbers
        assert valid_palindrome("1a1") == True
        # Not palindrome with numbers
        assert valid_palindrome("1a2") == False
    
    def test_case_insensitivity(self):
        """Test that the solution is case-insensitive."""
        assert valid_palindrome("Aa") == True
        assert valid_palindrome("Aba") == True
        assert valid_palindrome("ABa") == True
        assert valid_palindrome("MadAm") == True
        
    def test_performance(self):
        """Test performance characteristics."""
        # All same character
        all_same = "a" * 10000
        assert valid_palindrome(all_same) == True
        
        # Large palindrome
        large_palindrome = "a" * 10000 + "bcb" + "a" * 10000
        assert valid_palindrome(large_palindrome) == True
        
        # Large non-palindrome
        large_string = "a" * 10000 + "bca" + "a" * 10000
        assert valid_palindrome(large_string) == False


if __name__ == "__main__":
    pytest.main([__file__])
