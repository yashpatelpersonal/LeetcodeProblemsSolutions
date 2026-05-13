class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=prices[0]
        max_pr=0
        for i in prices:
            min_=min(i,min_)
            diff=i-min_
            max_pr=max(diff,max_pr)
        return max_pr

# if __name__ == '__main__':
#     s= Solution()
#     max_r=s.maxProfit(prices=[7,1,5,3,6,4])
#     print(max_r)