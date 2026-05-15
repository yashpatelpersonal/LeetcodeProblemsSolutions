class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices : return 0
        ind=0
        dp=[0 for _ in range(len(prices))]
        for k in range(1,3):
            min_=-prices[0]
            pr=0
            for i in range(1,len(prices)):
                min_=max(min_,dp[i]-prices[i])
                pr=max(pr,min_+prices[i])
                dp[i]=pr
                ind=i
        return dp[ind]

# if __name__ == '__main__':
#     s= Solution()
#     max_r=s.maxProfit(prices=[3,3,5,0,0,3,1,4])
#     print(max_r)