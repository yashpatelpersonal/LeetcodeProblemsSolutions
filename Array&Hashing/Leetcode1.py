#Problem: Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
class Solution:
    def twoSum(self,nums,target):
        ret_=[]
        for i in range(len(nums)):
            rem=target-nums[i]
            if i not in ret_ and rem in nums[i+1:]:
                ret_.append(i)
                if rem == nums[i]:
                    ret_.append(nums.index(rem,i+1))
                else:
                    ret_.append(nums.index(rem))
        return list(set(ret_))


if __name__ == '__main__':
    s=Solution()
    return_list=s.twoSum(nums=[2,7,11,19],target=9)
    print(" index of target",return_list)