#154 find minimun value in array using min steps

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_=0
        high=len(nums)-1
        while min_<high:
            mid= min_+(high-min_)//2
            if nums[mid] > nums[high]: min_= mid+1
            elif nums[mid] > nums[min_]: high=mid
            else: high-=1
        return nums[high]
# if __name__ == '__main__':
#     s= Solution()
#     min_=s.findMin(nums=[3,4,5,1,2])
#     print(min_)