// Given a stock price vector,calculate the max profit of it, 
//you can take multiple transactions,but only one transaction at a time. 


// the stratage is to find the increasing sections in the vector. If the ith value is larger than (i-1)th, we will add their subtraction to the max_profit. 

int maxProfit(vector<int> &prices) {
        if (prices.empty()) return 0;
        int max_profit=0;
        for (int i=1;i<prices.size();++i){
            if (prices[i]>prices[i-1]) max_profit+=prices[i]-prices[i-1];
        }
        return max_profit;
    }
    <link href="http://alexgorbatchev.com/pub/sh/current/styles/shThemeDefault.css" rel="stylesheet" type="text/css" />
<script src="http://alexgorbatchev.com/pub/sh/current/scripts/shCore.js" type="text/javascript"></script>
<script src="http://alexgorbatchev.com/pub/sh/current/scripts/shAutoloader.js" type="text/javascript"></script>
