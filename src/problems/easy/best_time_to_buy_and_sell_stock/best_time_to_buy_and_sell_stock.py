"""
Best Time To Buy And Sell Stock Problem

This module contains the main solution interface and method stubs for different approaches.
"""

from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_index = None
        min_index = None
        lowest_tracked_index = None

        for i in range(len(prices)):

            if max_index is None:
                max_index = i
                min_index = i
                continue
                
            if prices[i] >= prices[max_index]:
                max_index = i
                # if tracked min is not None then we want to update it here
                if lowest_tracked_index is not None:
                    min_index = lowest_tracked_index
                    lowest_tracked_index = None
                continue

            if (prices[i] < prices[min_index]):
                if lowest_tracked_index is None or prices[i] < prices[lowest_tracked_index]:
                    lowest_tracked_index = i
                
        return prices[max_index] - prices[min_index] 


def best_time_to_buy_and_sell_stock(prices: List[int]) -> int:
    """
    Main function for best time to buy and sell stock problem.
    
    Args:
        prices: List of stock prices for each day
        
    Returns:
        Maximum profit achievable from one transaction
    """
    solution = Solution()
    return solution.maxProfit(prices)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices1}")
    print(f"Output: {solution.maxProfit(prices1)}")
    
    # Example 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"\nInput: {prices2}")
    print(f"Output: {solution.maxProfit(prices2)}")
