# Selection Sort

## Overview
Selection sort is a simple comparison-based sorting algorithm. It repeatedly finds the minimum element from the unsorted portion and places it at the beginning.

## Algorithm Steps
1. **Find the minimum**: Scan the unsorted portion to find the smallest element
2. **Swap**: Exchange it with the first element of the unsorted portion
3. **Repeat**: Continue for the remaining unsorted elements

## Key Characteristics
- **In-place**: Modifies the original array
- **Not stable**: May change the relative order of equal elements
- **Not adaptive**: Always performs the same number of comparisons regardless of input order

## Time Complexity
- **Best case**: O(n²) - still needs to scan all elements
- **Average case**: O(n²)
- **Worst case**: O(n²) - always does maximum comparisons

## Space Complexity
- **O(1)** - Only uses a few extra variables (min_val, min_index, i, j)

## Example Walkthrough
```
Array: [64, 25, 12, 22, 11]

Pass 1: Find min in [64, 25, 12, 22, 11] → 11
        Swap: [11, 25, 12, 22, 64]

Pass 2: Find min in [25, 12, 22, 64] → 12
        Swap: [11, 12, 25, 22, 64]

Pass 3: Find min in [25, 22, 64] → 22
        Swap: [11, 12, 22, 25, 64]

Pass 4: Find min in [25, 64] → 25 (already in place)
        Result: [11, 12, 22, 25, 64] ✓
```

## When to Use
- Simple implementation needed
- Small datasets
- Memory is limited (in-place sorting)
- Understanding sorting fundamentals

## When NOT to Use
- Large datasets (O(n²) is too slow)
- Real-world applications (use quicksort, mergesort, or built-in sort)
- Stability is required (use stable sort instead)

## Implementation Details

### The Swap
```python
# Pythonic tuple unpacking
nums[i], nums[min_index] = nums[min_index], nums[i]
```

### Finding the Minimum
```python
# Track both value and index
min_val = nums[i]
min_index = i

# Update when finding smaller element
if nums[j] < min_val:
    min_val = nums[j]
    min_index = j
```

## Strengths
✅ Simple to understand and implement  
✅ In-place sorting (O(1) space)  
✅ No dependency on input data distribution  
✅ Easy to explain to beginners  

## Weaknesses
❌ Slow for large datasets (O(n²))  
❌ Not stable  
❌ Makes many unnecessary swaps  
❌ Poor cache performance due to non-sequential access  

## Comparison with Other Sorts
- **vs Bubble Sort**: Similar complexity, but selection sort makes fewer swaps
- **vs Quicksort**: Much slower, but simpler to understand
- **vs Insertion Sort**: Similar but slightly less efficient due to always scanning unsorted portion

