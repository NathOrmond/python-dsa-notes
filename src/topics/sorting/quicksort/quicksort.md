# Quick Sort

## Overview
Quicksort is a divide-and-conquer comparison-based sorting algorithm. It works by choosing a "pivot" element and partitioning the array such that elements smaller than the pivot come before it and elements greater come after it.

## Algorithm Steps (Divide & Conquer)
1. **Base case**: If array has ≤ 1 element, it's sorted
2. **Pivot**: Choose an element as the pivot
3. **Partition**: Rearrange elements so pivot is in correct position
4. **Recurse**: Recursively sort left and right sub-arrays

## Key Characteristics
- **Efficient**: O(n log n) average case
- **In-place** (depending on implementation)
- **Not stable**: Equal elements may be reordered
- **Recursive**: Uses recursion to sort sub-arrays

## Time Complexity
- **Best case**: O(n log n) - balanced partitions
- **Average case**: O(n log n) - random pivots perform well
- **Worst case**: O(n²) - unbalanced partitions (already sorted with bad pivot choice)

## Space Complexity
- **This implementation**: O(n) - creates new lists
- **In-place version**: O(log n) - recursion stack depth

## Pivot Selection Strategies
1. **First element**: Simple but can cause worst case
2. **Last element**: Similar to first
3. **Middle element**: Better on average
4. **Random**: Minimizes worst case probability ✅ (this implementation)
5. **Median-of-three**: Robust choice for real-world use

## Example Walkthrough
```
Array: [64, 25, 12, 22, 11]

Step 1: Choose pivot (random) → 22
        Partition: [12, 11] [22] [64, 25]
        
Step 2: Sort left [12, 11]
        Pivot → 12
        Partition: [11] [12] []
        Result: [11, 12]
        
Step 3: Sort right [64, 25]
        Pivot → 25
        Partition: [] [25] [64]
        Result: [25, 64]
        
Final: [11, 12] + [22] + [25, 64] = [11, 12, 22, 25, 64] ✓
```

## When to Use
- General-purpose sorting (fast average case)
- Large datasets
- Real-world applications
- When O(n log n) performance is acceptable

## When NOT to Use
- Worst case performance must be guaranteed (use mergesort)
- Stability is required (use stable sort)
- Very limited memory (consider heapsort)
- Simple sorting needed (insertion sort better for small arrays)

## Implementation Details

### Base Case
```python
if len(nums) < 2:
    return nums  # Already sorted!
```

### Choosing Pivot
```python
# Random pivot reduces worst case probability
pivot_idx = random.randint(0, len(nums) - 1)
pivot = nums[pivot_idx]
```

### Partitioning
```python
# Create two lists around pivot
smaller = []  # Elements < pivot
greater = []  # Elements >= pivot

# Skip pivot to avoid duplicates
for i in range(len(nums)):
    if i == pivot_idx:
        continue
    if nums[i] < pivot:
        smaller.append(nums[i])
    else:
        greater.append(nums[i])
```

### Recursive Call
```python
# Python list concatenation with +
return self.quick_sort(smaller) + [pivot] + self.quick_sort(greater)
```

## Strengths
✅ Fast average case: O(n log n)  
✅ In-place when implemented properly  
✅ Good cache performance  
✅ Practical for most real-world use  
✅ Locality of reference (works well with CPU cache)  

## Weaknesses
❌ Worst case O(n²) without good pivot strategy  
❌ Not stable by default  
❌ Performance degrades on sorted/reverse-sorted data with bad pivot  
❌ Recursive implementation can cause stack overflow on very large arrays  

## Improvements
1. **Insertion sort for small arrays**: Hybrid approach
2. **Median-of-three pivot**: Better pivot selection
3. **Three-way partitioning**: Handles duplicates better
4. **Iterative implementation**: Avoid recursion overhead
5. **Tail recursion optimization**: Reduce stack usage

## Comparison with Other Sorts
- **vs Selection Sort**: Much faster (O(n log n) vs O(n²))
- **vs Merge Sort**: Faster in practice, but not stable
- **vs Heap Sort**: Better cache performance, but worse worst case
- **vs Bubble Sort**: Dramatically faster

## Notes on This Implementation
This implementation creates new lists (`smaller` and `greater`) rather than sorting in-place. This makes it:
- Easier to understand
- O(n) space instead of O(log n)
- More Pythonic
- Simpler to implement

For a production-ready in-place version, you'd use Hoare's partition or Lomuto's partition scheme.

