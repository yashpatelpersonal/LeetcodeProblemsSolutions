# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
#
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
#
#
#
# Example 1:
#
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.
# Example 2:
#
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
#
#


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_1 =min(nums1)
        min_2 =min(nums2)
        print(min_1,min_2)
        if min_1 <= min_2:
            if min_1 not in nums2 and min_2 in nums1:
                return min_2
            elif min_2 not in nums1 and min_1 in nums2:
                return min_1
            elif min_2== min_1:
                return min_2




if __name__ == '__main__':
    s=Solution()
    n=s.getCommon(nums1=[1000000000,1000000000],nums2=[1000000000])
    print(n)