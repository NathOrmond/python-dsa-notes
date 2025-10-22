# Python Data Structures and Algorithms

This repository is for learning and practicing data structures and algorithms using Python.

---

## Project Structure

- `src/`: Contains the implementation of various data structures and algorithms.
   - `problems/`: Contains leetcode style problems
      - `easy/`: Contains leetcode easies
      - `medium/`: leetcode mediums
      - `hard/`: leetcode hards
   - `topics/`: Specific dsa related topics with a focus
- `tests/`: Contains unit tests for the code in `src/` -- mirrors directory structure of `src/`.

---

## Problem-Solving Methodology

### Step 1: Problem Analysis
1. **Write the problem description** in a `.md` file (e.g., `two_sum.md`)
2. **Create method stubs only** in the main solution file (e.g., `two_sum.py`) with:
   - Proper type hints
   - Docstrings describing the approach
   - Empty implementation (return placeholder values)

### Step 2: Test-Driven Development
1. **Write comprehensive unit tests** before implementing solutions
2. Tests should cover:
   - Basic examples from the problem
   - Edge cases
   - Boundary conditions
   - Multiple solution approaches

### Step 3: Solution Architecture
Each problem follows this structure:

```
src/problems/{difficulty}/{problem_name}/
├── {problem_name}.py          # Main solution file (solution-agnostic)
├── {problem_name}.md          # Problem description
├── solutions/
│   ├── solution_1.py          # First approach (e.g., brute force)
│   ├── solution_2.py          # Optimized approach (e.g., hash map)
│   └── solution_3.py          # Alternative approach (if applicable)
└── explanations/
    ├── approach_1.md          # Explanation of first solution
    ├── approach_2.md          # Explanation of second solution
    └── complexity_analysis.md # Time/space complexity comparison
```

### Step 4: Implementation Strategy
1. **Main file (`{problem_name}.py`)**:
   - Contains the "official" solution interface
   - Should be solution-agnostic (no specific algorithm implementation)
   - Acts as the primary API for the problem

2. **Solution files (`solutions/solution_X.py`)**:
   - Each file contains a complete implementation of one approach
   - Includes detailed comments explaining the algorithm
   - Can be imported and tested independently

3. **Explanation files (`explanations/`)**:
   - Detailed walkthrough of each approach
   - Complexity analysis
   - Trade-offs between different solutions

### Example Workflow
1. Read `two_sum.md` to understand the problem
2. Write tests in `tests/problems/easy/test_two_sum.py`
3. Create method stubs in `two_sum.py`
4. Implement `solutions/solution_1.py` (brute force)
5. Implement `solutions/solution_2.py` (hash map)
6. Write explanations for each approach
7. Update main `two_sum.py` with the preferred solution

## Getting Started

1. Clone the repository:
   ```bash
   git clone git@github.com:NathOrmond/python-dsa-notes.git
   ```
2. Install the dependencies:
   ```bash
   make install
   # or: pip install -r requirements.txt
   ```
3. Configure environment (optional):
   ```bash
   # Copy environment template
   make setup-env
   
   # Edit .env to customize settings
   # **RECOMMENDED** -- Uncomment PYTHONPYCACHEPREFIX for centralized cache
   ```
4. Run the tests:
   ```bash
   make test
   # or: pytest
   ```

## Quick Commands

```bash
# Check your progress
make status

# Create a new problem
make create-problem DIFFICULTY=easy NAME=valid_parentheses

# Run specific tests
make test-two-sum

# Benchmark performance
make benchmark-two-sum

# Track learning progress
python scripts/track_progress.py --report

# Cache management
make clean-cache          # Remove __pycache__ directories
make setup-cache          # Set up centralized cache directory

# Environment setup
make setup-env            # Copy env.example to .env

# Grind 75 setup
make setup-grind75        # Generate all 75 Grind 75 problems
```

## Available Scripts

- `scripts/check_solutions.py` - Check implementation status
- `scripts/create_problem.py` - Generate new problem structure
- `scripts/benchmark.py` - Performance benchmarking
- `scripts/track_progress.py` - Learning progress tracker
- `scripts/setup_cache.py` - Configure Python cache settings
- `scripts/generate_grind75.py` - Generate all Grind 75 problems

## Templates

- `templates/__init__.py.template` - Template for auto-importing `__init__.py` files
- `env.example` - Environment configuration template

## Grind 75 Problems

This project includes all 75 problems from the [Grind 75](https://www.techinterviewhandbook.org/grind75) list:

- **Easy**: 24 problems
- **Medium**: 42 problems  
- **Hard**: 9 problems

Each problem includes:
- ✅ Method stubs with type hints and docstrings
- ✅ Comprehensive test cases
- ✅ Problem description template
- ✅ Multiple solution approaches (brute force + optimized)
- ✅ Auto-importing package structure

To get started with Grind 75:
```bash
make setup-grind75  # Generate all 75 problems
make status         # Check your progress
```

---

## Learning Workflow

### For Each Problem:

1. **Read the Problem Description**
   ```bash
   # Read the .md file to understand the problem
   cat src/problems/easy/two_sum/two_sum.md
   ```

2. **Implement Solutions**
   - Start with the brute force approach in `solutions/solution_1.py`
   - Then implement the optimized approach in `solutions/solution_2.py`
   - Update the main functions in `two_sum.py` as you complete them

3. **Test Your Solutions**
   ```bash
   # Run tests to see which solutions pass/fail
   python -m pytest tests/problems/easy/test_two_sum.py -v
   
   # Or run the test status checker
   python scripts/check_solutions.py
   ```

4. **Check Your Progress**
   ```bash
   # See implementation status across all problems
   python scripts/check_solutions.py --all
   ```

### Solution Status Tracking

The test runner will show you:
- ✅ **Implemented**: Solution is complete and passes all tests
- ❌ **Failed**: Solution is implemented but has bugs
- ⏳ **Not Implemented**: Solution is just a stub (returns `None` or raises `NotImplementedError`)

### Example Learning Session

```bash
# 1. Check current status
python scripts/check_solutions.py

# 2. Implement brute force solution
# Edit: src/problems/easy/two_sum/solutions/solution_1.py
# Edit: src/problems/easy/two_sum/two_sum.py (two_sum_brute_force function)

# 3. Test your implementation
python -m pytest tests/problems/easy/test_two_sum.py::TestTwoSumBruteForce -v

# 4. Implement hash map solution
# Edit: src/problems/easy/two_sum/solutions/solution_2.py
# Edit: src/problems/easy/two_sum/two_sum.py (two_sum_hash_map function)

# 5. Test all solutions
python -m pytest tests/problems/easy/test_two_sum.py -v

# 6. Check final status
python scripts/check_solutions.py
```

---

## Development Guidelines

- **Always write tests first** - This ensures you understand the problem requirements
- **Start with brute force** - Get a working solution before optimizing
- **Document your thinking** - Use comments and explanation files to track your learning
- **Compare approaches** - Understanding trade-offs is crucial for interviews
- **Focus on clarity** - Readable code is more important than clever one-liners
- **Test frequently** - Run tests after each implementation to catch bugs early
