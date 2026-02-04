# Best Time to Buy and Sell Stock

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Examples

### Example 1:
**Input:** `prices = [7,1,5,3,6,4]`  
**Output:** `5`  
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.  
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2:
**Input:** `prices = [7,6,4,3,1]`  
**Output:** `0`  
**Explanation:** In this case, no transactions are done and the max profit = 0.

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Approach

### Track Min and Max Approach
The approach tracks three indices while iterating through the prices:
- `max_index` - tracks the index with the highest price seen
- `min_index` - tracks the minimum price we've bought at (that we can still use)
- `lowest_tracked_index` - temporarily tracks a new low that might be better

When a new maximum is found:
- Update `max_index`
- If there's a `lowest_tracked_index`, it becomes the new `min_index` (since we found a better buy point)
- Clear `lowest_tracked_index`

When prices drop below current `min_index`:
- Track this in `lowest_tracked_index` as a potential better buy point
- Only update when this new low is lower than any previously tracked low

## Time Complexity

O(n) where n is the length of the prices array  
- Single pass through the array

## Space Complexity

O(1)  
- Only using a constant number of variables to track indices

## Related Problems

- [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
- [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
