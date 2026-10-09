class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0, sell = buy + 1, maxProfit = 0;

        while(sell < prices.length) {
            int diff = prices[sell] - prices[buy];
            if(maxProfit < diff) { maxProfit = diff; }
            if(diff < 0) { buy++; sell=buy;}
            sell++;
        }

        return maxProfit;
    }
}
