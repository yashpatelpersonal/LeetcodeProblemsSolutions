class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum=sum(nums)
        left_sum=0
        output_list=[]
        for i in nums:
            total_sum-=i
            output_list.append(abs(left_sum-total_sum))
            left_sum+=i
        return output_list

if __name__ == '__main__':
    sol=Solution()
    sum_list=sol.leftRightDifference(nums=[10,4,8,3])
    print(sum_list)