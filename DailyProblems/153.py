#Problem 153
#Leetcode 153 find minimum value in array using n(log n)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_=nums[0]
        for key, value in enumerate(nums):
            if nums[key] < min_  :
                min_=nums[key]
        return min_


if __name__ == '__main__':
    s= Solution()
    min_=s.findMin(nums=[3,4,5,1,2])
    print(min_)