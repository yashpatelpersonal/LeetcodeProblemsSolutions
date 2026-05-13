class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_count=[1] * len(nums)
        prefix=1
        for i in range(len(nums)):
            list_count[i]=prefix
            prefix*=nums[i]
        post_fix=1
        for i in range(len(nums)-1,-1,-1):
            list_count[i]*=post_fix
            post_fix*=nums[i]
        return list_count











