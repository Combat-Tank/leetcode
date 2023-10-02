class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        delta = 0
        max_delta = 0
        min_element = prices[0]
        for i in range(1,len(prices)):
            delta = prices[i] - min_element
            if(delta > max_delta):
                max_delta = delta
            if(prices[i] < min_element):
                min_element = prices[i]

        return max_delta