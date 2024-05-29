#leetcode practice link --- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1269100663/

#youtube link -- https://www.youtube.com/watch?v=excAOvwF_Wk

class Solution:
    def BuyandSellStocks(self, n, prices):
        mini = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            cost = prices[i] - mini
            profit = max(profit, cost)
            mini = min(mini, prices[i])
        return profit

s = Solution()
print(s.BuyandSellStocks(6, [7, 1, 5, 3, 6, 4]))


#OUTPUT
# 5