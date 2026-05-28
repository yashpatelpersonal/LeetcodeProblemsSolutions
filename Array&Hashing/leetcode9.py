
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if "".join(list(reversed(str(x))))==str(x):
            return True
        else:
            return False


