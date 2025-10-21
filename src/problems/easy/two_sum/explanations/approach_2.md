# Two Sum - Hash Map Approach

## Algorithm Overview
The hash map approach is the optimal solution for the Two Sum problem. Instead of checking every pair, we use a dictionary to store numbers we've already seen and their indices, allowing us to find complements in constant time.

## Key Insight
If we're looking for two numbers that sum to `target`, and we're currently at number `nums[i]`, then we need to find `target - nums[i]` somewhere in the array. If we've already seen this complement, we can immediately return the solution.

## Step-by-Step Process
1. **Initialize**: Create an empty dictionary `num_to_index = {}`
2. **Iterate**: Go through each number `nums[i]` with its index `i`
3. **Calculate Complement**: For current number `nums[i]`, calculate `complement = target - nums[i]`
4. **Check Dictionary**: If `complement` exists in our dictionary, return `[num_to_index[complement], i]`
5. **Store Current**: Add `nums[i]` and its index `i` to the dictionary
6. **Continue**: Move to the next number

## Code Walkthrough
```python
def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    num_to_index = {}  # {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If we've seen the complement before, we found our pair
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Store current number for future lookups
        num_to_index[num] = i
    
    raise ValueError("No solution found")
```

## Why This Works
- **Efficiency**: Dictionary lookups are O(1) on average
- **Single Pass**: We only need to iterate through the array once
- **Memory Trade-off**: We use extra space to gain significant time improvement

## When to Use
- **Production Code**: This is the preferred solution for real applications
- **Large Input**: Scales well with input size
- **Interview**: Demonstrates understanding of time-space trade-offs

## Advantages
- **Time Complexity**: O(n) instead of O(n²)
- **Scalable**: Performs well even with large inputs
- **Elegant**: Clean, readable solution

## Trade-offs
- **Space Usage**: Uses O(n) extra space for the hash map
- **Memory**: Requires additional memory proportional to input size
