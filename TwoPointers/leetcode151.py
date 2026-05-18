import re

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        rever=s[::-1]
        _re_white_space = re.compile(r"\s+")
        r=_re_white_space.sub(" ", " ".join(rever)).strip()
        return r


# if __name__ == '__main__':
#     s= Solution()
#     s.reverseWords(s="a good   example")