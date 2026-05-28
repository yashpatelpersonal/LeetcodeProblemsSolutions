class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        nums_copy=nums.copy()
        for i in nums_copy:
            if i == val:
                nums.remove(i)
        return len(nums)


# if __name__ == '__main__':
#     s=Solution()
#     result=s.removeElement(nums=[0,1,2,2,3,0,4,2],val=2)
