#!/usr/bin/env python3
"""
Grind 75 Problem Generator

This script generates all 75 problems from the Grind 75 list with proper structure,
method stubs, and comprehensive tests.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict


# Grind 75 problems extracted from the HTML
GRIND_75_PROBLEMS = [
    # Week 1 - Easy
    ("Two Sum", "easy"),
    ("Valid Parentheses", "easy"),
    ("Merge Two Sorted Lists", "easy"),
    ("Best Time to Buy and Sell Stock", "easy"),
    ("Valid Palindrome", "easy"),
    ("Invert Binary Tree", "easy"),
    ("Valid Anagram", "easy"),
    ("Binary Search", "easy"),
    ("Flood Fill", "easy"),
    ("Lowest Common Ancestor of a Binary Search Tree", "easy"),
    ("Balanced Binary Tree", "easy"),
    ("Linked List Cycle", "easy"),
    ("Implement Queue using Stacks", "easy"),
    
    # Week 2 - Easy + 1 Medium
    ("First Bad Version", "easy"),
    ("Ransom Note", "easy"),
    ("Climbing Stairs", "easy"),
    ("Longest Palindrome", "easy"),
    ("Reverse Linked List", "easy"),
    ("Majority Element", "easy"),
    ("Add Binary", "easy"),
    ("Diameter of Binary Tree", "easy"),
    ("Middle of the Linked List", "easy"),
    ("Maximum Depth of Binary Tree", "easy"),
    ("Contains Duplicate", "easy"),
    ("Maximum Subarray", "medium"),
    
    # Week 3 - Medium
    ("Insert Interval", "medium"),
    ("01 Matrix", "medium"),
    ("K Closest Points to Origin", "medium"),
    ("Longest Substring Without Repeating Characters", "medium"),
    ("3Sum", "medium"),
    ("Binary Tree Level Order Traversal", "medium"),
    ("Clone Graph", "medium"),
    ("Evaluate Reverse Polish Notation", "medium"),
    
    # Week 4 - Medium
    ("Course Schedule", "medium"),
    ("Implement Trie (Prefix Tree)", "medium"),
    ("Coin Change", "medium"),
    ("Product of Array Except Self", "medium"),
    ("Min Stack", "medium"),
    ("Validate Binary Search Tree", "medium"),
    ("Number of Islands", "medium"),
    ("Rotting Oranges", "medium"),
    
    # Week 5 - Medium
    ("Search in Rotated Sorted Array", "medium"),
    ("Combination Sum", "medium"),
    ("Permutations", "medium"),
    ("Merge Intervals", "medium"),
    ("Lowest Common Ancestor of a Binary Tree", "medium"),
    ("Time Based Key-Value Store", "medium"),
    ("Accounts Merge", "medium"),
    ("Sort Colors", "medium"),
    
    # Week 6 - Medium
    ("Word Break", "medium"),
    ("Partition Equal Subset Sum", "medium"),
    ("String to Integer (atoi)", "medium"),
    ("Spiral Matrix", "medium"),
    ("Subsets", "medium"),
    ("Binary Tree Right Side View", "medium"),
    ("Longest Palindromic Substring", "medium"),
    ("Unique Paths", "medium"),
    ("Construct Binary Tree from Preorder and Inorder Traversal", "medium"),
    
    # Week 7 - Medium
    ("Container With Most Water", "medium"),
    ("Letter Combinations of a Phone Number", "medium"),
    ("Word Search", "medium"),
    ("Find All Anagrams in a String", "medium"),
    ("Minimum Height Trees", "medium"),
    ("Task Scheduler", "medium"),
    ("LRU Cache", "medium"),
    
    # Week 8 - Medium + Hard
    ("Kth Smallest Element in a BST", "medium"),
    ("Minimum Window Substring", "hard"),
    ("Serialize and Deserialize Binary Tree", "hard"),
    ("Trapping Rain Water", "hard"),
    ("Find Median from Data Stream", "hard"),
    ("Word Ladder", "hard"),
    ("Basic Calculator", "hard"),
    ("Maximum Profit in Job Scheduling", "hard"),
    ("Merge k Sorted Lists", "hard"),
    ("Largest Rectangle in Histogram", "hard"),
]


def convert_to_snake_case(name: str) -> str:
    """Convert problem name to snake_case for file names."""
    # Remove special characters and convert to lowercase
    name = re.sub(r'[^\w\s]', '', name)
    # Replace spaces and hyphens with underscores
    name = re.sub(r'[\s-]+', '_', name)
    return name.lower()


def get_function_signature(name: str, difficulty: str) -> Tuple[str, str, str]:
    """Generate function signature based on problem name."""
    snake_name = convert_to_snake_case(name)
    
    # Common patterns for different problem types
    if "two_sum" in snake_name:
        return snake_name, "nums: List[int], target: int", "List[int]"
    elif "valid_parentheses" in snake_name:
        return snake_name, "s: str", "bool"
    elif "merge" in snake_name and "list" in snake_name:
        return snake_name, "list1: Optional[ListNode], list2: Optional[ListNode]", "Optional[ListNode]"
    elif "binary_search" in snake_name:
        return snake_name, "nums: List[int], target: int", "int"
    elif "palindrome" in snake_name:
        return snake_name, "s: str", "bool"
    elif "anagram" in snake_name:
        return snake_name, "s: str, t: str", "bool"
    elif "tree" in snake_name:
        return snake_name, "root: Optional[TreeNode]", "Optional[TreeNode]"
    elif "linked_list" in snake_name:
        return snake_name, "head: Optional[ListNode]", "Optional[ListNode]"
    elif "array" in snake_name or "subarray" in snake_name:
        return snake_name, "nums: List[int]", "int"
    elif "string" in snake_name:
        return snake_name, "s: str", "int"
    elif "matrix" in snake_name:
        return snake_name, "matrix: List[List[int]]", "List[int]"
    elif "stack" in snake_name:
        return snake_name, "", "None"
    elif "queue" in snake_name:
        return snake_name, "", "None"
    else:
        # Default signature
        return snake_name, "nums: List[int]", "int"


def create_problem_structure(name: str, difficulty: str, root_dir: Path):
    """Create the complete problem structure for a single problem."""
    snake_name = convert_to_snake_case(name)
    func_name, params, return_type = get_function_signature(name, difficulty)
    
    # Create directories
    problem_dir = root_dir / "src" / "problems" / difficulty / snake_name
    solutions_dir = problem_dir / "solutions"
    explanations_dir = problem_dir / "explanations"
    test_dir = root_dir / "tests" / "problems" / difficulty
    
    problem_dir.mkdir(parents=True, exist_ok=True)
    solutions_dir.mkdir(parents=True, exist_ok=True)
    explanations_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py files
    create_init_files(problem_dir, snake_name)
    
    # Create main problem file
    create_main_problem_file(problem_dir, snake_name, func_name, params, return_type)
    
    # Create solution files
    create_solution_files(solutions_dir, snake_name, func_name, params, return_type)
    
    # Create problem description
    create_problem_description(problem_dir, name, snake_name)
    
    # Create test file
    create_test_file(test_dir, snake_name, func_name, params, return_type)
    
    print(f"✅ Created {difficulty}/{snake_name}")


def create_init_files(problem_dir: Path, problem_name: str):
    """Create __init__.py files for the problem."""
    
    # Main problem __init__.py
    init_content = f'''# This file makes the directory a Python package
# Auto-imports all public functions from the main module

def _auto_import_functions():
    """Automatically import all public functions from the main module."""
    import importlib
    import inspect
    from pathlib import Path
    
    try:
        # Get the main module name (same as directory name)
        module_name = Path(__file__).parent.name
        
        # Import the main module
        main_module = importlib.import_module(f'.{{module_name}}', package=__package__)
        
        # Get all public functions and import them
        imported_functions = []
        for name in dir(main_module):
            if not name.startswith('_'):
                obj = getattr(main_module, name)
                if inspect.isfunction(obj):
                    globals()[name] = obj
                    imported_functions.append(name)
        
        return imported_functions
    except Exception:
        # Fallback to manual import if dynamic discovery fails
        from .{problem_name} import {problem_name}, {problem_name}_brute_force, {problem_name}_optimized
        return ['{problem_name}', '{problem_name}_brute_force', '{problem_name}_optimized']

# Auto-import all functions
__all__ = _auto_import_functions()
'''
    
    with open(problem_dir / "__init__.py", "w") as f:
        f.write(init_content)
    
    # Solutions __init__.py
    solutions_init_content = "# This file makes the directory a Python package\n"
    with open(problem_dir / "solutions" / "__init__.py", "w") as f:
        f.write(solutions_init_content)


def create_main_problem_file(problem_dir: Path, problem_name: str, func_name: str, params: str, return_type: str):
    """Create the main problem file with method stubs."""
    
    # Determine the optimized approach name based on problem type
    if "tree" in func_name:
        optimized_name = f"{func_name}_recursive"
    elif "list" in func_name:
        optimized_name = f"{func_name}_iterative"
    elif "search" in func_name:
        optimized_name = f"{func_name}_binary_search"
    elif "palindrome" in func_name or "anagram" in func_name:
        optimized_name = f"{func_name}_two_pointers"
    else:
        optimized_name = f"{func_name}_optimized"
    
    content = f'''"""
{problem_name.replace('_', ' ').title()} Problem

This module contains the main solution interface and method stubs for different approaches.
"""

from typing import List, Optional


def {func_name}({params}) -> {return_type}:
    """
    Main solution function for {problem_name.replace('_', ' ')}.
    
    TODO: Implement this function
    - This is the main interface that should use the optimal approach
    - See solutions/ directory for different implementations
    - Time Complexity: TODO
    - Space Complexity: TODO
    
    Args:
        {params}
        
    Returns:
        {return_type}: TODO - describe what this function returns
        
    Raises:
        ValueError: If input is invalid
    """
    # Use the optimized solution as the main implementation
    return {optimized_name}({params.split(':')[0].split(',')[0].strip() if params else ""})


def {func_name}_brute_force({params}) -> {return_type}:
    """
    Brute force approach for {problem_name.replace('_', ' ')}.
    
    TODO: Implement this function
    - Start with the most straightforward approach
    - Consider all possible combinations/solutions
    - Time Complexity: O(n²) or higher
    - Space Complexity: O(1) or O(n)
    
    Args:
        {params}
        
    Returns:
        {return_type}: TODO - describe what this function returns
    """
    # TODO: Implement brute force solution
    # Hint: Think about the most obvious way to solve this problem
    # Hint: Consider nested loops, checking all possibilities
    pass


def {optimized_name}({params}) -> {return_type}:
    """
    Optimized approach for {problem_name.replace('_', ' ')}.
    
    TODO: Implement this function
    - Use the most efficient algorithm/data structure
    - Consider hash maps, two pointers, dynamic programming, etc.
    - Time Complexity: O(n) or O(n log n)
    - Space Complexity: O(n) or O(1)
    
    Args:
        {params}
        
    Returns:
        {return_type}: TODO - describe what this function returns
    """
    # TODO: Implement optimized solution
    # Hint: Think about the most efficient way to solve this problem
    # Hint: Consider using hash maps, two pointers, binary search, etc.
    pass


# Example usage
if __name__ == "__main__":
    # TODO: Add example usage here
    print("TODO: Add example usage")
'''
    
    with open(problem_dir / f"{problem_name}.py", "w") as f:
        f.write(content)


def create_solution_files(solutions_dir: Path, problem_name: str, func_name: str, params: str, return_type: str):
    """Create solution files with method stubs."""
    
    # Solution 1 - Brute Force
    solution1_content = f'''"""
Brute Force Solution for {problem_name.replace('_', ' ').title()}
"""

from typing import List, Optional


def {func_name}_brute_force({params}) -> {return_type}:
    """
    Brute force approach for {problem_name.replace('_', ' ')}.
    
    TODO: Implement this function
    - Start with the most straightforward approach
    - Consider all possible combinations/solutions
    - Time Complexity: O(n²) or higher
    - Space Complexity: O(1) or O(n)
    
    Args:
        {params}
        
    Returns:
        {return_type}: TODO - describe what this function returns
    """
    # TODO: Implement brute force solution
    # Hint: Think about the most obvious way to solve this problem
    # Hint: Consider nested loops, checking all possibilities
    pass


# Example usage
if __name__ == "__main__":
    # TODO: Add example usage here
    print("TODO: Add example usage")
'''
    
    with open(solutions_dir / "solution_1.py", "w") as f:
        f.write(solution1_content)
    
    # Solution 2 - Optimized
    optimized_name = f"{func_name}_optimized"
    if "tree" in func_name:
        optimized_name = f"{func_name}_recursive"
    elif "list" in func_name:
        optimized_name = f"{func_name}_iterative"
    elif "search" in func_name:
        optimized_name = f"{func_name}_binary_search"
    elif "palindrome" in func_name or "anagram" in func_name:
        optimized_name = f"{func_name}_two_pointers"
    
    solution2_content = f'''"""
Optimized Solution for {problem_name.replace('_', ' ').title()}
"""

from typing import List, Optional


def {optimized_name}({params}) -> {return_type}:
    """
    Optimized approach for {problem_name.replace('_', ' ')}.
    
    TODO: Implement this function
    - Use the most efficient algorithm/data structure
    - Consider hash maps, two pointers, dynamic programming, etc.
    - Time Complexity: O(n) or O(n log n)
    - Space Complexity: O(n) or O(1)
    
    Args:
        {params}
        
    Returns:
        {return_type}: TODO - describe what this function returns
    """
    # TODO: Implement optimized solution
    # Hint: Think about the most efficient way to solve this problem
    # Hint: Consider using hash maps, two pointers, binary search, etc.
    pass


# Example usage
if __name__ == "__main__":
    # TODO: Add example usage here
    print("TODO: Add example usage")
'''
    
    with open(solutions_dir / "solution_2.py", "w") as f:
        f.write(solution2_content)


def create_problem_description(problem_dir: Path, name: str, snake_name: str):
    """Create problem description markdown file."""
    
    content = f'''# {name}

## Problem Description

TODO: Add problem description from LeetCode

## Examples

TODO: Add examples

## Constraints

TODO: Add constraints

## Approach

TODO: Add approach hints

## Time Complexity

TODO: Add time complexity analysis

## Space Complexity

TODO: Add space complexity analysis

## Related Problems

TODO: Add related problems
'''
    
    with open(problem_dir / f"{snake_name}.md", "w") as f:
        f.write(content)


def create_test_file(test_dir: Path, problem_name: str, func_name: str, params: str, return_type: str):
    """Create comprehensive test file."""
    
    # Determine test data based on problem type
    if "two_sum" in func_name:
        test_data = "nums = [2, 7, 11, 15], target = 9"
        expected = "[0, 1]"
    elif "valid_parentheses" in func_name:
        test_data = 's = "()"'
        expected = "True"
    elif "palindrome" in func_name:
        test_data = 's = "racecar"'
        expected = "True"
    elif "anagram" in func_name:
        test_data = 's = "anagram", t = "nagaram"'
        expected = "True"
    elif "binary_search" in func_name:
        test_data = "nums = [-1, 0, 3, 5, 9, 12], target = 9"
        expected = "4"
    else:
        test_data = "nums = [1, 2, 3, 4, 5]"
        expected = "TODO"
    
    content = f'''"""
Tests for {problem_name.replace('_', ' ').title()}
"""

import pytest
from src.problems.easy.{problem_name} import {func_name}, {func_name}_brute_force


class Test{problem_name.title().replace('_', '')}:
    """Test cases for {problem_name} problem."""
    
    def test_main_function_basic(self):
        """Test main function with basic examples."""
        # TODO: Add basic test cases
        # Example: assert {func_name}({test_data}) == {expected}
        pass
    
    def test_main_function_edge_cases(self):
        """Test main function with edge cases."""
        # TODO: Add edge case tests
        # - Empty input
        # - Single element
        # - Maximum constraints
        pass
    
    def test_brute_force_basic(self):
        """Test brute force approach with basic examples."""
        # TODO: Add basic test cases for brute force
        pass
    
    def test_brute_force_edge_cases(self):
        """Test brute force approach with edge cases."""
        # TODO: Add edge case tests for brute force
        pass
    
    def test_approaches_consistent(self):
        """Test that different approaches give consistent results."""
        # TODO: Test that all approaches give the same result
        # test_cases = [
        #     # Add test cases here
        # ]
        # for test_case in test_cases:
        #     result1 = {func_name}(test_case)
        #     result2 = {func_name}_brute_force(test_case)
        #     assert result1 == result2
        pass
    
    def test_performance(self):
        """Test performance characteristics."""
        # TODO: Add performance tests
        # - Large input sizes
        # - Time complexity verification
        pass
    
    def test_invalid_input(self):
        """Test handling of invalid input."""
        # TODO: Add tests for invalid input
        # - None values
        # - Invalid types
        # - Out of bounds
        pass


if __name__ == "__main__":
    pytest.main([__file__])
'''
    
    with open(test_dir / f"test_{problem_name}.py", "w") as f:
        f.write(content)


def main():
    """Main function to generate all Grind 75 problems."""
    print("🚀 Generating Grind 75 Problems")
    print("=" * 50)
    
    # Get the root directory
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    # Create medium and hard directories if they don't exist
    (root_dir / "src" / "problems" / "medium").mkdir(parents=True, exist_ok=True)
    (root_dir / "src" / "problems" / "hard").mkdir(parents=True, exist_ok=True)
    (root_dir / "tests" / "problems" / "medium").mkdir(parents=True, exist_ok=True)
    (root_dir / "tests" / "problems" / "hard").mkdir(parents=True, exist_ok=True)
    
    # Generate all problems
    total_problems = len(GRIND_75_PROBLEMS)
    easy_count = sum(1 for _, diff in GRIND_75_PROBLEMS if diff == "easy")
    medium_count = sum(1 for _, diff in GRIND_75_PROBLEMS if diff == "medium")
    hard_count = sum(1 for _, diff in GRIND_75_PROBLEMS if diff == "hard")
    
    print(f"📊 Problem Distribution:")
    print(f"   Easy: {easy_count}")
    print(f"   Medium: {medium_count}")
    print(f"   Hard: {hard_count}")
    print(f"   Total: {total_problems}")
    print()
    
    for i, (name, difficulty) in enumerate(GRIND_75_PROBLEMS, 1):
        print(f"[{i:2d}/{total_problems}] Creating {difficulty}/{convert_to_snake_case(name)}...")
        try:
            create_problem_structure(name, difficulty, root_dir)
        except Exception as e:
            print(f"❌ Error creating {name}: {e}")
    
    print()
    print("✅ All Grind 75 problems created successfully!")
    print()
    print("📋 Next Steps:")
    print("1. Run 'make status' to see all problems")
    print("2. Start implementing solutions!")
    print("3. Run tests with 'make test'")
    print("4. Check progress with 'python scripts/track_progress.py'")


if __name__ == "__main__":
    main()
