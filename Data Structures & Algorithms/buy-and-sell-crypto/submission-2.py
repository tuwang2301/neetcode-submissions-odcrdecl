class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = float('inf')
        # profit = 0

        # for p in prices:
        #     min_price = min(min_price, p)
        #     profit = max(profit, p - min_price)

        # return profit if profit > 0 else 0

        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(profit, max_p)
            else:
                l = r
            r += 1

        return max_p