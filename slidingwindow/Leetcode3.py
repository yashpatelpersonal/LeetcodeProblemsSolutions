class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_ch=set()
        left=0
        max_le=0
        for i in range(len(s)):
            while s[i] in char_ch:
                char_ch.remove(s[left])
                left+=1
            char_ch.add(s[i])
            max_le=max(max_le,i-left+1)
        return max_le


# s= Solution()
# val=s.lengthOfLongestSubstring(s="abcabcbb")
# print(val)