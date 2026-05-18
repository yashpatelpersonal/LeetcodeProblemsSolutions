class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for i in s :
            if i.isalnum():new_s+=i.lower()
        return new_s == new_s[::-1]

# if __name__ == '__main__':
#     s=Solution()
#     s.isPalindrome(s="A man, a plan, a canal: Panama")