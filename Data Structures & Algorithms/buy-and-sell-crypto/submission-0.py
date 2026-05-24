class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        prevPrice = 10000
        for price in prices:
            if price < prevPrice:
                prevPrice = price

            elif maxProfit < price - prevPrice:
                maxProfit = price - prevPrice

        return maxProfit