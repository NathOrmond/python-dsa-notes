"""
Tests for Best Time To Buy And Sell Stock
"""

import pytest
from src.problems.easy.best_time_to_buy_and_sell_stock import best_time_to_buy_and_sell_stock


class TestBestTimeToBuyAndSellStock:
    """Test cases for best_time_to_buy_and_sell_stock problem."""
    
    def test_basic_examples(self):
        """Test with basic examples."""
        # Example 1: Should return 5 (buy at 1, sell at 6)
        assert best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]) == 5
        
        # Example 2: No profit possible
        assert best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]) == 0
        
        # Single transaction with profit
        assert best_time_to_buy_and_sell_stock([2, 4, 1]) == 2
        
        # All increasing prices
        assert best_time_to_buy_and_sell_stock([1, 2, 3, 4, 5]) == 4
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Single element (no profit possible)
        assert best_time_to_buy_and_sell_stock([5]) == 0
        
        # Two elements with profit
        assert best_time_to_buy_and_sell_stock([1, 2]) == 1
        
        # Two elements without profit
        assert best_time_to_buy_and_sell_stock([2, 1]) == 0
        
        # All same price
        assert best_time_to_buy_and_sell_stock([3, 3, 3, 3]) == 0
        
        # Best buy happens before best sell
        assert best_time_to_buy_and_sell_stock([3, 2, 6, 5, 0, 3]) == 4
    
    def test_performance(self):
        """Test performance characteristics."""
        # Large array with profit
        large_array_profit = [i for i in range(1000, 0, -1)] + [2000, 1500]
        assert best_time_to_buy_and_sell_stock(large_array_profit) >= 1500
        
        # Large array without profit
        large_array_no_profit = list(range(1000, 0, -1))
        assert best_time_to_buy_and_sell_stock(large_array_no_profit) == 0


if __name__ == "__main__":
    pytest.main([__file__])
