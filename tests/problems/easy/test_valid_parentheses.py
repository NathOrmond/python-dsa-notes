"""
Tests for Valid Parentheses
"""

import pytest
from src.problems.easy.valid_parentheses import valid_parentheses


class TestValidParentheses:
    """Test cases for valid_parentheses problem."""
    
    def test_main_function_basic(self):
        """Test main function with basic examples."""
        # Test cases from problem description
        assert valid_parentheses("()") == True
        assert valid_parentheses("()[]{}") == True
        assert valid_parentheses("(]") == False
        assert valid_parentheses("([])") == True
        assert valid_parentheses("([)]") == False
    
    def test_main_function_edge_cases(self):
        """Test main function with edge cases."""
        # Empty string - should be valid (no brackets to validate)
        assert valid_parentheses("") == True
        
        # Single opening bracket
        assert valid_parentheses("(") == False
        assert valid_parentheses("[") == False
        assert valid_parentheses("{") == False
        
        # Single closing bracket
        assert valid_parentheses(")") == False
        assert valid_parentheses("]") == False
        assert valid_parentheses("}") == False
        
        # Only opening brackets
        assert valid_parentheses("(((") == False
        assert valid_parentheses("[[[") == False
        assert valid_parentheses("{{{") == False
        
        # Only closing brackets
        assert valid_parentheses(")))") == False
        assert valid_parentheses("]]]") == False
        assert valid_parentheses("}}}") == False
        
        # Mixed unmatched brackets
        assert valid_parentheses("([)]") == False
        assert valid_parentheses("{[}]") == False
        assert valid_parentheses("(]") == False
    
    
    def test_performance(self):
        """Test performance characteristics."""
        # Test with maximum constraint size (10^4 characters)
        large_valid = "(" * 5000 + ")" * 5000
        large_invalid = "(" * 5000 + "]" * 5000
        
        # These should complete quickly
        assert valid_parentheses(large_valid) == True
        assert valid_parentheses(large_invalid) == False
    
    def test_invalid_input(self):
        """Test handling of invalid input."""
        # Note: The problem constraints state s consists of parentheses only
        # So we don't need to handle None or invalid characters
        # But we can test edge cases within the constraints
        
        # Test with very long strings (within constraint)
        very_long_valid = "()" * 5000
        very_long_invalid = "(" * 10000  # All opening brackets
        
        assert valid_parentheses(very_long_valid) == True
        assert valid_parentheses(very_long_invalid) == False


if __name__ == "__main__":
    pytest.main([__file__])
