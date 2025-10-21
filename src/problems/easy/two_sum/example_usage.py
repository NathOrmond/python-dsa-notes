#!/usr/bin/env python3
"""
Example usage of Two Sum solutions.

This script demonstrates how to use the different approaches
and shows the performance difference between them.
"""

import time
from two_sum import two_sum, two_sum_brute_force, two_sum_hash_map


def demonstrate_solutions():
    """Demonstrate different Two Sum solutions."""
    
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 8),
        ([0, 4, 3, 0], 0),
    ]
    
    print("Two Sum Problem Solutions")
    print("=" * 50)
    
    for nums, target in test_cases:
        print(f"\nInput: nums={nums}, target={target}")
        
        # Main solution (hash map)
        result = two_sum(nums, target)
        print(f"Main solution: {result}")
        
        # Brute force
        result_bf = two_sum_brute_force(nums, target)
        print(f"Brute force:   {result_bf}")
        
        # Hash map
        result_hm = two_sum_hash_map(nums, target)
        print(f"Hash map:      {result_hm}")
        
        # Verify all solutions are consistent
        assert set(result) == set(result_bf) == set(result_hm)
        print("✓ All solutions consistent")


def performance_comparison():
    """Compare performance of different approaches."""
    
    print("\nPerformance Comparison")
    print("=" * 50)
    
    # Create a larger test case
    nums = list(range(1000)) + [1999, 2000]
    target = 3999
    
    print(f"Testing with {len(nums)} elements...")
    
    # Test brute force
    start_time = time.time()
    result_bf = two_sum_brute_force(nums, target)
    bf_time = time.time() - start_time
    
    # Test hash map
    start_time = time.time()
    result_hm = two_sum_hash_map(nums, target)
    hm_time = time.time() - start_time
    
    print(f"Brute force result: {result_bf} (Time: {bf_time:.6f}s)")
    print(f"Hash map result:    {result_hm} (Time: {hm_time:.6f}s)")
    print(f"Speedup: {bf_time/hm_time:.1f}x faster with hash map")


if __name__ == "__main__":
    demonstrate_solutions()
    performance_comparison()
