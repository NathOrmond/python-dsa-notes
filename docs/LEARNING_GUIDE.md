# DSA Learning Quick Reference

## Getting Started
```bash
# Check your current progress
python scripts/check_solutions.py

# Run tests to see what's failing
python -m pytest tests/problems/easy/test_two_sum.py -v
```

### Centralized Bytecode Cache (Recommended)
Keep your repo clean by centralizing `.pyc` files (Python 3.8+):
```bash
make setup-cache
echo 'PYTHONPYCACHEPREFIX=.cache/python' >> .env
source setup_env.sh  # or use Make targets which auto-load .env
```

### Cleanup
```bash
python scripts/clean_caches.py            # delete caches/build artifacts
python scripts/clean_caches.py --dry-run  # preview only
```

## 📝 Implementation Workflow

### 1. Read the Problem
```bash
cat src/problems/easy/two_sum/two_sum.md
```

### 2. Implement Brute Force Solution
Edit: `src/problems/easy/two_sum/solutions/solution_1.py`
```python
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    # TODO: Implement nested loops
    # Hint: for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    pass
```

### 3. Test Your Implementation
```bash
python -m pytest tests/problems/easy/test_two_sum.py::TestTwoSumBruteForce -v
```

### 4. Implement Hash Map Solution
Edit: `src/problems/easy/two_sum/solutions/solution_2.py`
```python
def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    # TODO: Implement hash map approach
    # Hint: num_to_index = {}
    #       for i, num in enumerate(nums):
    #           complement = target - num
    pass
```

### 5. Update Main Functions
Edit: `src/problems/easy/two_sum/two_sum.py`
- Copy your implementations from solution files
- Update `two_sum_brute_force()` and `two_sum_hash_map()`

### 6. Final Testing
```bash
python -m pytest tests/problems/easy/test_two_sum.py -v
python scripts/check_solutions.py
```

## 🎯 Success Indicators
- ✅ All tests pass
- ✅ Solution status shows "Implemented"
- ✅ You understand both approaches
- ✅ You can explain the time/space complexity

## 📚 Learning Resources
- Read explanations in `explanations/` directory
- Compare your solution with the hints in the code
- Understand why one approach is faster than the other
