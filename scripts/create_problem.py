#!/usr/bin/env python3
"""
Problem Generator

Creates a new DSA problem following the established project structure.
"""

import os
import sys
import argparse
from pathlib import Path


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


def create_problem_structure(difficulty: str, problem_name: str, root_dir: Path):
    """Create the complete problem structure."""
    
    # Create main directories
    problem_dir = root_dir / "src" / "problems" / difficulty / problem_name
    solutions_dir = problem_dir / "solutions"
    explanations_dir = problem_dir / "explanations"
    test_dir = root_dir / "tests" / "problems" / difficulty
    
    # Create directories
    problem_dir.mkdir(parents=True, exist_ok=True)
    solutions_dir.mkdir(parents=True, exist_ok=True)
    explanations_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py files
    create_init_files(problem_dir, problem_name)
    
    # Create main problem file
    create_main_problem_file(problem_dir, problem_name)
    
    # Create solution files
    create_solution_files(solutions_dir, problem_name)
    
    # Create explanation templates
    create_explanation_templates(explanations_dir, problem_name)
    
    # Create test file
    create_test_file(test_dir, problem_name)
    
    # Create problem description template
    create_problem_description(problem_dir, problem_name)
    
    print(f"✅ Created problem structure for {difficulty}/{problem_name}")
    print(f"📁 Problem directory: {problem_dir}")
    print(f"🧪 Test file: {test_dir}/test_{problem_name}.py")


def create_main_problem_file(problem_dir: Path, problem_name: str):
    """Create the main problem solution file."""
    
    content = f'''"""
{problem_name.replace('_', ' ').title()} Problem

TODO: Add problem description here
"""

from typing import List


def {problem_name}(nums: List[int], target: int) -> List[int]:
    """
    Main solution function.
    
    TODO: Implement the optimal solution here
    
    Args:
        nums: Input array
        target: Target value
        
    Returns:
        Solution result
    """
    # Use the optimal approach as the main implementation
    return {problem_name}_optimized(nums, target)


def {problem_name}_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach.
    
    TODO: Implement brute force solution
    - Time Complexity: O(?)
    - Space Complexity: O(?)
    """
    # TODO: Implement brute force solution
    pass


def {problem_name}_optimized(nums: List[int], target: int) -> List[int]:
    """
    Optimized approach.
    
    TODO: Implement optimized solution
    - Time Complexity: O(?)
    - Space Complexity: O(?)
    """
    # TODO: Implement optimized solution
    pass
'''
    
    with open(problem_dir / f"{problem_name}.py", "w") as f:
        f.write(content)


def create_solution_files(solutions_dir: Path, problem_name: str):
    """Create solution files."""
    
    # Solution 1 (Brute Force)
    solution_1_content = f'''"""
{problem_name.replace('_', ' ').title()} - Brute Force Solution

TODO: Add description of brute force approach

Time Complexity: O(?) - TODO: Fill in
Space Complexity: O(?) - TODO: Fill in
"""

from typing import List


def {problem_name}_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach.
    
    TODO: Implement this function
    - Add implementation hints here
    - Time Complexity: O(?)
    - Space Complexity: O(?)
    
    Args:
        nums: Input array
        target: Target value
        
    Returns:
        Solution result
    """
    # TODO: Implement brute force solution
    # Hint: Start with the most straightforward approach
    pass


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        # TODO: Add test cases here
    ]
    
    for test_input, expected in test_cases:
        result = {problem_name}_brute_force(*test_input)
        print(f"Input: {{test_input}}")
        print(f"Output: {{result}}")
        print(f"Expected: {{expected}}")
        print(f"Correct: {{result == expected}}")
        print("-" * 40)
'''
    
    # Solution 2 (Optimized)
    solution_2_content = f'''"""
{problem_name.replace('_', ' ').title()} - Optimized Solution

TODO: Add description of optimized approach

Time Complexity: O(?) - TODO: Fill in
Space Complexity: O(?) - TODO: Fill in
"""

from typing import List


def {problem_name}_optimized(nums: List[int], target: int) -> List[int]:
    """
    Optimized approach.
    
    TODO: Implement this function
    - Add implementation hints here
    - Time Complexity: O(?)
    - Space Complexity: O(?)
    
    Args:
        nums: Input array
        target: Target value
        
    Returns:
        Solution result
    """
    # TODO: Implement optimized solution
    # Hint: Think about data structures that can help
    pass


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        # TODO: Add test cases here
    ]
    
    for test_input, expected in test_cases:
        result = {problem_name}_optimized(*test_input)
        print(f"Input: {{test_input}}")
        print(f"Output: {{result}}")
        print(f"Expected: {{expected}}")
        print(f"Correct: {{result == expected}}")
        print("-" * 40)
'''
    
    with open(solutions_dir / "solution_1.py", "w") as f:
        f.write(solution_1_content)
    
    with open(solutions_dir / "solution_2.py", "w") as f:
        f.write(solution_2_content)


def create_explanation_templates(explanations_dir: Path, problem_name: str):
    """Create explanation template files."""
    
    # Approach 1 explanation
    approach_1_content = f'''# {problem_name.replace('_', ' ').title()} - Brute Force Approach

## Algorithm Overview
TODO: Describe the brute force approach

## Step-by-Step Process
1. TODO: Step 1
2. TODO: Step 2
3. TODO: Step 3

## Code Walkthrough
```python
def {problem_name}_brute_force(nums, target):
    # TODO: Add code walkthrough
    pass
```

## Why This Works
- TODO: Explain correctness
- TODO: Explain completeness

## When to Use
- TODO: When is this approach appropriate?

## Limitations
- TODO: What are the drawbacks?
'''
    
    # Approach 2 explanation
    approach_2_content = f'''# {problem_name.replace('_', ' ').title()} - Optimized Approach

## Algorithm Overview
TODO: Describe the optimized approach

## Key Insight
TODO: What's the key insight that makes this faster?

## Step-by-Step Process
1. TODO: Step 1
2. TODO: Step 2
3. TODO: Step 3

## Code Walkthrough
```python
def {problem_name}_optimized(nums, target):
    # TODO: Add code walkthrough
    pass
```

## Why This Works
- TODO: Explain correctness
- TODO: Explain efficiency

## When to Use
- TODO: When is this approach preferred?

## Advantages
- TODO: What are the benefits?

## Trade-offs
- TODO: What are the costs?
'''
    
    # Complexity analysis
    complexity_content = f'''# {problem_name.replace('_', ' ').title()} - Complexity Analysis

## Time Complexity Comparison

| Approach | Time Complexity | Explanation |
|----------|----------------|-------------|
| Brute Force | O(?) | TODO: Explain |
| Optimized | O(?) | TODO: Explain |

## Space Complexity Comparison

| Approach | Space Complexity | Explanation |
|----------|------------------|-------------|
| Brute Force | O(?) | TODO: Explain |
| Optimized | O(?) | TODO: Explain |

## Detailed Analysis

### Brute Force Approach
- **Time**: O(?)
  - TODO: Detailed analysis
- **Space**: O(?)
  - TODO: Detailed analysis

### Optimized Approach
- **Time**: O(?)
  - TODO: Detailed analysis
- **Space**: O(?)
  - TODO: Detailed analysis

## Performance Comparison

For different input sizes:

| Input Size (n) | Brute Force | Optimized | Speedup |
|----------------|-------------|-----------|---------|
| 100 | ~? ops | ~? ops | ?x |
| 1,000 | ~? ops | ~? ops | ?x |
| 10,000 | ~? ops | ~? ops | ?x |

## When to Choose Each Approach

### Choose Brute Force When:
- TODO: When to use brute force

### Choose Optimized When:
- TODO: When to use optimized

## Real-World Considerations

### Memory Usage
- TODO: Memory considerations

### Implementation Complexity
- TODO: Implementation considerations

### Interview Context
- TODO: Interview tips
'''
    
    with open(explanations_dir / "approach_1.md", "w") as f:
        f.write(approach_1_content)
    
    with open(explanations_dir / "approach_2.md", "w") as f:
        f.write(approach_2_content)
    
    with open(explanations_dir / "complexity_analysis.md", "w") as f:
        f.write(complexity_content)


def create_test_file(test_dir: Path, problem_name: str):
    """Create test file template."""
    
    test_content = f'''"""
Test cases for {problem_name.replace('_', ' ').title()} problem.

This file demonstrates the test-driven development approach:
1. Write comprehensive tests first
2. Cover basic examples, edge cases, and boundary conditions
3. Test multiple solution approaches
"""

import pytest
from typing import List

# Import the main solution functions
from src.problems.easy.{problem_name} import {problem_name}, {problem_name}_brute_force, {problem_name}_optimized

# Import individual solution implementations
from src.problems.easy.{problem_name}.solutions.solution_1 import {problem_name}_brute_force as brute_force_impl
from src.problems.easy.{problem_name}.solutions.solution_2 import {problem_name}_optimized as optimized_impl


class Test{problem_name.title().replace('_', '')}:
    """Test cases for the main {problem_name} function."""
    
    def test_example_1(self):
        """Test case from problem description."""
        # TODO: Add test case
        pass
    
    def test_example_2(self):
        """Test case from problem description."""
        # TODO: Add test case
        pass


class Test{problem_name.title().replace('_', '')}BruteForce:
    """Test cases for brute force approach."""
    
    @pytest.mark.parametrize("input_data,expected", [
        # TODO: Add parametrized test cases
    ])
    def test_brute_force_basic_cases(self, input_data, expected):
        """Test basic functionality of brute force approach."""
        result = brute_force_impl(*input_data)
        assert result == expected
    
    def test_brute_force_edge_cases(self):
        """Test edge cases for brute force approach."""
        # TODO: Add edge case tests
        pass


class Test{problem_name.title().replace('_', '')}Optimized:
    """Test cases for optimized approach."""
    
    @pytest.mark.parametrize("input_data,expected", [
        # TODO: Add parametrized test cases
    ])
    def test_optimized_basic_cases(self, input_data, expected):
        """Test basic functionality of optimized approach."""
        result = optimized_impl(*input_data)
        assert result == expected
    
    def test_optimized_edge_cases(self):
        """Test edge cases for optimized approach."""
        # TODO: Add edge case tests
        pass


class TestSolutionConsistency:
    """Test that both approaches produce valid results."""
    
    @pytest.mark.parametrize("input_data", [
        # TODO: Add test cases
    ])
    def test_approaches_consistent(self, input_data):
        """Test that both approaches produce valid results."""
        brute_result = brute_force_impl(*input_data)
        optimized_result = optimized_impl(*input_data)
        
        # TODO: Add consistency checks
        pass


class TestPerformance:
    """Performance tests to demonstrate complexity differences."""
    
    def test_large_input_brute_force(self):
        """Test brute force with larger input."""
        # TODO: Add performance test
        pass
    
    def test_large_input_optimized(self):
        """Test optimized with larger input."""
        # TODO: Add performance test
        pass


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__])
'''
    
    with open(test_dir / f"test_{problem_name}.py", "w") as f:
        f.write(test_content)


def create_problem_description(problem_dir: Path, problem_name: str):
    """Create problem description template."""
    
    content = f'''# Problem: {problem_name.replace('_', ' ').title()}

TODO: Add problem description here

## Example 1:

**Input:** TODO
**Output:** TODO
**Explanation:** TODO

## Example 2:

**Input:** TODO
**Output:** TODO

## Example 3:

**Input:** TODO
**Output:** TODO

## Constraints:

- TODO: Add constraints
- TODO: Add constraints
- TODO: Add constraints
'''
    
    with open(problem_dir / f"{problem_name}.md", "w") as f:
        f.write(content)


def main():
    """Main function to create a new problem."""
    parser = argparse.ArgumentParser(description="Create a new DSA problem")
    parser.add_argument("difficulty", choices=["easy", "medium", "hard"], help="Problem difficulty")
    parser.add_argument("problem_name", help="Name of the problem (snake_case)")
    
    args = parser.parse_args()
    
    # Get the root directory (parent of scripts directory)
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    create_problem_structure(args.difficulty, args.problem_name, root_dir)


if __name__ == "__main__":
    main()
