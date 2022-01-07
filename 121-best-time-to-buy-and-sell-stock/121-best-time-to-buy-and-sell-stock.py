class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmax = 0
        globalmax = 0
        
        for i in range(1, len(prices)):
            currmax = max(0, currmax + prices[i] - prices[i-1])
            globalmax = max(currmax, globalmax)
            
        return globalmax