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
    init_content = f'''# This package exposes a single canonical solution function
from .{problem_name} import {problem_name}

__all__ = [
    '{problem_name}',
]
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
    
    # Create solution files (optional additional approaches)
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
    Solution function for {problem_name.replace('_', ' ')}.
    
    TODO: Implement this function
    - Time Complexity: TODO
    - Space Complexity: TODO
    
    Args:
        nums: Input array
        target: Target value
        
    Returns:
        Solution result
    """
    # TODO: Implement your solution
    pass
'''
    
    with open(problem_dir / f"{problem_name}.py", "w") as f:
        f.write(content)


def create_solution_files(solutions_dir: Path, problem_name: str):
    """Create solution files."""
    
    # Create a single simple solution file (optional, not auto-exported)
    solution_content = f'''"""
{problem_name.replace('_', ' ').title()} Solution

TODO: Add solution approach description here

Time Complexity: TODO
Space Complexity: TODO
"""

from typing import List


def {problem_name}(nums: List[int], target: int) -> List[int]:
    """
    Solution for {problem_name.replace('_', ' ')}.
    
    TODO: Implement this function
    - Add your solution here
    - Time Complexity: TODO
    - Space Complexity: TODO
    
    Args:
        nums: Input array
        target: Target value
        
    Returns:
        Solution result
    """
    # TODO: Implement your solution
    pass


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        # TODO: Add test cases here
    ]
    
    for test_input, expected in test_cases:
        result = {problem_name}(*test_input)
        print(f"Input: {{test_input}}")
        print(f"Output: {{result}}")
        print(f"Expected: {{expected}}")
        print(f"Correct: {{result == expected}}")
        print("-" * 40)
'''
    
    with open(solutions_dir / "solution_1.py", "w") as f:
        f.write(solution_content)


def create_explanation_templates(explanations_dir: Path, problem_name: str):
    """Create explanation template files."""
    
    # Approach 1 explanation
    approach_1_content = f'''# {problem_name.replace('_', ' ').title()} - Approach 1

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
    approach_2_content = f'''# {problem_name.replace('_', ' ').title()} - Approach 2

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
"""

import pytest

from src.problems.easy.{problem_name} import {problem_name}


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


if __name__ == "__main__":
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
