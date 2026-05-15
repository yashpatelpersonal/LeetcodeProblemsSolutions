class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        reversed_n = int(str(x)[::-1])
        if reversed_n <= -2**31 or reversed_n >= (2**31)-1:
            return 0
        return reversed_n * sign

if __name__ == '__main__':
    s= Solution()
    r=s.reverse(x=123)
    print(r)