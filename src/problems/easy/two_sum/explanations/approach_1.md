# Two Sum - Brute Force Approach

## Algorithm Overview
The brute force approach is the most straightforward solution to the Two Sum problem. We simply check every possible pair of numbers in the array to see if they sum to the target.

## Step-by-Step Process
1. **Initialize**: Start with the first number at index `i`
2. **Nested Loop**: For each number at index `i`, check all subsequent numbers at index `j` (where `j > i`)
3. **Check Sum**: For each pair `(nums[i], nums[j])`, check if `nums[i] + nums[j] == target`
4. **Return Result**: If a pair is found, return `[i, j]`

## Code Walkthrough
```python
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    
    # Check every pair of numbers
    for i in range(n):                    # Outer loop: first number
        for j in range(i + 1, n):         # Inner loop: second number
            if nums[i] + nums[j] == target:
                return [i, j]             # Found the pair!
    
    raise ValueError("No solution found")
```

## Why This Works
- **Completeness**: We check every possible pair, so we're guaranteed to find the solution if it exists
- **Correctness**: The problem states there's exactly one solution, so we'll find it
- **Simplicity**: Easy to understand and implement

## When to Use
- **Learning**: Great for understanding the problem
- **Small Input**: When `n` is very small (< 100 elements)
- **Interview**: Shows you can solve the problem, even if not optimally

## Limitations
- **Performance**: O(n²) time complexity makes it slow for large inputs
- **Scalability**: Doesn't scale well with input size
