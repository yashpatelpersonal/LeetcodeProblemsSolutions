class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        index=0
        for i in costs:
            if count+i<= coins:
                count+=i
                index+=1
        return index