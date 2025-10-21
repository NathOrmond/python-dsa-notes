"""
Test cases for Valid Parentheses problem.

This file demonstrates the test-driven development approach:
1. Write comprehensive tests first
2. Cover basic examples, edge cases, and boundary conditions
3. Test multiple solution approaches
"""

import pytest
from typing import List

# Import the main solution functions
from src.problems.easy.valid_parentheses import valid_parentheses, valid_parentheses_brute_force, valid_parentheses_stack

# Import individual solution implementations
from src.problems.easy.valid_parentheses.solutions.solution_1 import valid_parentheses_brute_force as brute_force_impl
from src.problems.easy.valid_parentheses.solutions.solution_2 import valid_parentheses_stack as stack_impl


class TestValidParentheses:
    """Test cases for the main valid_parentheses function."""
    
    def test_example_1(self):
        """Test case from problem description."""
        assert valid_parentheses("()") == True
    
    def test_example_2(self):
        """Test case from problem description."""
        assert valid_parentheses("()[]{}") == True
    
    def test_example_3(self):
        """Test case from problem description."""
        assert valid_parentheses("(]") == False
    
    def test_example_4(self):
        """Test case from problem description."""
        assert valid_parentheses("([)]") == False
    
    def test_example_5(self):
        """Test case from problem description."""
        assert valid_parentheses("{[]}") == True


class TestValidParenthesesBruteForce:
    """Test cases for brute force approach."""
    
    @pytest.mark.parametrize("s,expected", [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),  # Empty string is valid
        ("(", False),  # Unclosed bracket
        (")", False),  # Unopened bracket
    ])
    def test_brute_force_basic_cases(self, s, expected):
        """Test basic functionality of brute force approach."""
        result = brute_force_impl(s)
        assert result == expected
    
    def test_brute_force_edge_cases(self):
        """Test edge cases for brute force approach."""
        # Single character
        assert brute_force_impl("(") == False
        assert brute_force_impl(")") == False
        
        # Nested brackets
        assert brute_force_impl("((()))") == True
        assert brute_force_impl("((())") == False
        
        # Mixed brackets
        assert brute_force_impl("{[()]}") == True
        assert brute_force_impl("{[()]") == False


class TestValidParenthesesStack:
    """Test cases for stack approach."""
    
    @pytest.mark.parametrize("s,expected", [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),  # Empty string is valid
        ("(", False),  # Unclosed bracket
        (")", False),  # Unopened bracket
    ])
    def test_stack_basic_cases(self, s, expected):
        """Test basic functionality of stack approach."""
        result = stack_impl(s)
        assert result == expected
    
    def test_stack_edge_cases(self):
        """Test edge cases for stack approach."""
        # Single character
        assert stack_impl("(") == False
        assert stack_impl(")") == False
        
        # Nested brackets
        assert stack_impl("((()))") == True
        assert stack_impl("((())") == False
        
        # Mixed brackets
        assert stack_impl("{[()]}") == True
        assert stack_impl("{[()]") == False
        
        # Complex nested cases
        assert stack_impl("(([]){})") == True
        assert stack_impl("(([]){") == False


class TestSolutionConsistency:
    """Test that both approaches produce the same results."""
    
    @pytest.mark.parametrize("s", [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "",
        "(",
        ")",
        "((()))",
        "{[()]}",
        "(([]){})",
    ])
    def test_approaches_consistent(self, s):
        """Test that both approaches produce the same result."""
        brute_result = brute_force_impl(s)
        stack_result = stack_impl(s)
        
        # Both should produce the same result
        assert brute_result == stack_result


class TestPerformance:
    """Performance tests to demonstrate complexity differences."""
    
    def test_large_input_brute_force(self):
        """Test brute force with larger input."""
        # Create a large valid string
        large_string = "(" * 1000 + ")" * 1000
        result = brute_force_impl(large_string)
        assert result == True
    
    def test_large_input_stack(self):
        """Test stack with larger input."""
        # Create a large valid string
        large_string = "(" * 1000 + ")" * 1000
        result = stack_impl(large_string)
        assert result == True


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__])
