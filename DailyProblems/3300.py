#Leetcode 3300 :
#Mininum Element after replacement with Digit Sum
#Created By : Yashkumar Patel
class Solution:
    def minElement(self, nums: List[int]) -> int:
        list_min = []
        for i in nums:
            sum_v=0
            for j in str(i):
                sum_v+=int(j)
            list_min.append(sum_v)
        return min(list_min)


# if __name__ == '__main__':
#     s=Solution()
#     min_result=s.minElement(nums=[10,12,13,14])
#     print("list of min",min_result)
#
