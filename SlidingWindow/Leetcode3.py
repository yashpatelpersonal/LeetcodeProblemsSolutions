class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_ch=set()
        left=0
        max_le=0
        for r in range(len(s)):
            while s[r] in char_ch:
                char_ch.remove(s[left])
                left+=1
            char_ch.add(s[r])
            max_le=max(max_le,r-left+1)
        return max_le


# s= Solution()
# val=s.lengthOfLongestSubstring(s="abcabcbb")
# print(val)