"""
Tests for Valid Anagram
"""

import pytest
from src.problems.easy.valid_anagram import valid_anagram


class TestValidAnagram:
    """Test cases for valid_anagram problem."""
    
    def test_basic_examples(self):
        """Test with basic examples."""
        # Example 1: Classic anagram
        assert valid_anagram("anagram", "nagaram") == True
        # Example 2: Not an anagram
        assert valid_anagram("rat", "car") == False
        # Example 3: Same string
        assert valid_anagram("listen", "listen") == True
        # Example 4: Anagram with different word
        assert valid_anagram("listen", "silent") == True
        # Example 5: Not an anagram (different characters)
        assert valid_anagram("hello", "world") == False
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Empty strings (both empty)
        assert valid_anagram("", "") == True
        # Single character (same)
        assert valid_anagram("a", "a") == True
        # Single character (different)
        assert valid_anagram("a", "b") == False
        # Different lengths (should return False)
        assert valid_anagram("ab", "a") == False
        assert valid_anagram("a", "ab") == False
        # Same characters but different counts
        assert valid_anagram("aabb", "abab") == True
        assert valid_anagram("aabb", "abb") == False
        assert valid_anagram("aabb", "aab") == False
    
    def test_with_numbers_and_special_characters(self):
        """Test with numbers and special characters."""
        # Anagrams with numbers
        assert valid_anagram("123", "321") == True
        assert valid_anagram("12a3", "a321") == True
        # Not anagrams with numbers
        assert valid_anagram("123", "124") == False
        # Special characters
        assert valid_anagram("!@#", "#@!") == True
        assert valid_anagram("a!b", "b!a") == True
        assert valid_anagram("a!b", "b!c") == False
    
    def test_case_sensitivity(self):
        """Test case sensitivity (anagrams are typically case-sensitive)."""
        # Different cases should not be anagrams
        assert valid_anagram("A", "a") == False
        assert valid_anagram("Hello", "hello") == False
        # Same case anagrams
        assert valid_anagram("LISTEN", "SILENT") == True  # Both uppercase
        assert valid_anagram("listen", "silent") == True  # Both lowercase
        # Not anagrams even with same case
        assert valid_anagram("Tar", "Rat") == False  # T != R, not anagrams
        assert valid_anagram("Race", "Care") == False  # R != C, not anagrams
    
    def test_duplicate_characters(self):
        """Test with duplicate characters."""
        # Multiple duplicates
        assert valid_anagram("aabbcc", "ccbbaa") == True
        assert valid_anagram("aabbcc", "abcabc") == True
        # Different counts of duplicates
        assert valid_anagram("aaa", "aa") == False
        assert valid_anagram("aa", "aaa") == False
        # All same character
        assert valid_anagram("aaaa", "aaaa") == True
        assert valid_anagram("aaaa", "aaab") == False
    
    def test_performance(self):
        """Test performance characteristics."""
        # Large strings with same characters
        large_same = "a" * 10000
        assert valid_anagram(large_same, large_same) == True
        
        # Large strings that are anagrams
        large_anagram1 = "a" * 5000 + "b" * 5000
        large_anagram2 = "b" * 5000 + "a" * 5000
        assert valid_anagram(large_anagram1, large_anagram2) == True
        
        # Large strings that are not anagrams
        large_not_anagram1 = "a" * 5000 + "b" * 5000
        large_not_anagram2 = "a" * 5000 + "c" * 5000
        assert valid_anagram(large_not_anagram1, large_not_anagram2) == False
    
    def test_different_length_strings(self):
        """Test that different length strings return False."""
        # Various length mismatches
        assert valid_anagram("abc", "ab") == False
        assert valid_anagram("ab", "abc") == False
        assert valid_anagram("", "a") == False
        assert valid_anagram("a", "") == False
        assert valid_anagram("abcdef", "abc") == False


if __name__ == "__main__":
    pytest.main([__file__])
