class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n= len(nums)
        counter=1
        for i in range(n):
            if nums[i] != counter : return False
            if i < n -2 : counter+=1
        return n == nums[-1] + 1



# if __name__ == '__main__':
#     s= Solution ()
#     ans_=s.isGood(nums=([1,2,3,3,4]))
#     print("Permutation of array ",ans_)