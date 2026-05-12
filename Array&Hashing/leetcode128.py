class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        for i in nums:
            current=1
            for i in nums:
                 if i+1 in nums:
                     current+=1
        return max(current,max_len)


if __name__ == '__main__':
    s=Solution()
    print(s.longestConsecutive(nums=[1,100]))