# LeetCode 121. Best Time to Buy and Sell Stock (NeetCode 150)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Pattern: sliding-window
# Time: O(n)  Space: O(1)
# Insight:
#   - Why it works: scan right to left, keeping best_sell, the highest price seen to the
#     right. Each price is treated as the buy day, so its best profit is best_sell - price.
#     best_sell is updated after the profit is computed, so the sell day is always later
#     than the buy day.
#   - Conventional version: scan left to right, keeping min_price, the lowest price seen so
#     far. Each price is treated as the sell day, so its best profit is price - min_price.
#     It is the mirror image: "cheapest buy before today" instead of "best sell after today".
#         min_price = float('inf')
#         max_profit = 0
#         for price in prices:
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, price - min_price)
#         return max_profit
#   - Vs the naive approach: trying every buy/sell pair is O(n^2).
#   - Sliding window view (conventional version): the buy day is the left end and the current
#     day is the right end. When a lower price appears, the window restarts there, because a
#     lower buy price beats any earlier one for every later sell day.
#   - max_profit starts at 0, so if prices only fall, the answer is 0 and never negative.
#   - [PYTHONIC] reversed(prices) iterates backwards without copying the list, unlike
#     prices[::-1].
#   - [BUILT-IN] Alternative: itertools.accumulate gives the running minimum, and zip pairs
#     it with each price:
#         return max(p - m for p, m in zip(prices, accumulate(prices, min)))
# Interview Q&A:
#   Q: Why are the forward and reverse scans equivalent?
#   A: They fix the other end of the pair differently. Forward: for each sell day, the best buy
#      is the minimum before it. Reverse: for each buy day, the best sell is the maximum after it.
#      Both examine every day once as the fixed end.
#   Q: What if you can make as many transactions as you like (LeetCode 122)?
#   A: Add up every positive day-to-day difference. Greedy, O(n).
#   Q: What if you can make at most k transactions, or there is a cooldown (188, 309)?
#   A: Dynamic programming over states such as holding or not holding, and how many
#      transactions are used. For k transactions it is O(n * k).
#   Q: How do you return the buy and sell days, not just the profit?
#   A: Record the index whenever min_price is updated, and the (buy, sell) indices whenever
#      max_profit improves.
#   Q: What happens when prices only decrease?
#   A: The answer is 0, because max_profit starts at 0 and no negative profit is ever kept.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_sell = 0
        for price in reversed(prices):
            max_profit = max(max_profit, best_sell - price)
            best_sell = max(best_sell, price)
        return max_profit
