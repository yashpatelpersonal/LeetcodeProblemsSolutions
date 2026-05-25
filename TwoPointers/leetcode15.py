class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        list_set=set()
        for i in range(0,len(nums)):
            k=i+1
            j=k+1
            if j <= len(nums)-1:
                cal=nums[i]+nums[k]+nums[j]
                if cal == 0 :
                    a=sorted([nums[i],nums[k],nums[j]])
                    list_set.add((a[0],a[1],a[2]))
            # for k in range(i+1,len(nums)):
            #     for j in range(k+1,len(nums)):
            #         cal=nums[i]+nums[k]+nums[j]
        return [list(t) for t in list_set]



if __name__ == '__main__':
    s=Solution()
    re=s.threeSum(nums=[-1,0,1,2,-1,-4])
    print(re)

#
#
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         list_set=set()
#         for i in range(0,len(nums),2):
#             for k in range(i+1,len(nums)):
#                 for j in range(k+1,len(nums)):
#                     cal=nums[i]+nums[k]+nums[j]
#                     if cal == 0 :
#                         a=sorted([nums[i],nums[k],nums[j]])
#                         list_set.add((a[0],a[1],a[2]))
#         return [list(t) for t in list_set]
