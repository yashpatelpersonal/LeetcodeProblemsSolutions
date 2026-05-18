#Leetcode 1306
# Jump Game 3

class Solution:
    def rec(self,arr: List[int], i: int):
        if i <0 or i>=len(arr) or arr[i] <  0:
            return False
        if arr[i] == 0 : return True
        arr[i]*=-1
        left= self.rec(arr,i - arr[i] )
        right = self.rec(arr,i + arr[i])
        return left or right
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.rec(arr,start)