"""
Best Time To Buy And Sell Stock Problem

This module contains the main solution interface and method stubs for different approaches.
"""

from typing import List, Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        i_min = None
        for i in range(len(prices)):
            if i_min is None or prices[i] < prices[i_min]:
                i_min = i
                continue
            currProfit = prices[i] - prices[i_min]
            if currProfit > currMax:
                currMax = currProfit
        return currMax


def best_time_to_buy_and_sell_stock(prices: List[int]) -> int:
    """
    Main solution function for Best Time To Buy And Sell Stock.

    Uses a single pass to track the minimum price seen so far and the
    maximum profit achievable at each step.

    Args:
        prices: List of daily stock prices

    Returns:
        Maximum profit achievable from one buy and one sell (0 if none)
    """
    max_profit = 0
    min_price_so_far: Optional[int] = None

    for price in prices:
        if min_price_so_far is None or price < min_price_so_far:
            min_price_so_far = price
            continue
        profit = price - min_price_so_far
        if profit > max_profit:
            max_profit = profit

    return max_profit


    


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
