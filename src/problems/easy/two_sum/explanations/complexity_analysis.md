# Two Sum - Complexity Analysis

## Time Complexity Comparison

| Approach | Time Complexity | Explanation |
|----------|----------------|-------------|
| Brute Force | O(n²) | Nested loops: for each of n elements, check up to n-1 other elements |
| Hash Map | O(n) | Single pass through array, O(1) dictionary operations |

## Space Complexity Comparison

| Approach | Space Complexity | Explanation |
|----------|------------------|-------------|
| Brute Force | O(1) | Only uses a constant amount of extra space |
| Hash Map | O(n) | Dictionary can store up to n elements |

## Detailed Analysis

### Brute Force Approach
- **Time**: O(n²)
  - Outer loop runs n times
  - Inner loop runs (n-1) + (n-2) + ... + 1 = n(n-1)/2 times
  - Total operations: O(n²)
- **Space**: O(1)
  - Only uses variables for loop indices
  - No additional data structures

### Hash Map Approach
- **Time**: O(n)
  - Single pass through the array: O(n)
  - Dictionary operations (insert, lookup): O(1) average case
  - Total: O(n) × O(1) = O(n)
- **Space**: O(n)
  - Dictionary stores at most n elements
  - Each element is stored once

## Performance Comparison

For different input sizes:

| Input Size (n) | Brute Force | Hash Map | Speedup |
|----------------|-------------|----------|---------|
| 100 | ~5,000 ops | ~100 ops | 50x |
| 1,000 | ~500,000 ops | ~1,000 ops | 500x |
| 10,000 | ~50,000,000 ops | ~10,000 ops | 5,000x |

## When to Choose Each Approach

### Choose Brute Force When:
- Input size is very small (< 100 elements)
- Memory is extremely constrained
- You need to understand the problem first
- Implementing for educational purposes

### Choose Hash Map When:
- Input size is large or unknown
- Performance is important
- You're in a production environment
- You're optimizing for time over space

## Real-World Considerations

### Memory Usage
- Hash map approach uses more memory
- For very large datasets, this could be a concern
- Consider if the extra memory is worth the time savings

### Implementation Complexity
- Brute force is simpler to implement and debug
- Hash map requires understanding of dictionary operations
- Choose based on your team's expertise

### Interview Context
- Start with brute force to show you understand the problem
- Then optimize to hash map to show you can improve solutions
- Discuss trade-offs between time and space complexity
