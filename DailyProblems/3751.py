

class Solution:
    def waviness(self,num):
        s = str(num)
        if len(s) < 3:
            return 0
        count = 0
        for i in range(1, len(s) - 1):
            left = int(s[i - 1])
            curr = int(s[i])
            right = int(s[i + 1])
            if curr > left and curr > right:
                count += 1
            elif curr < left and curr < right:
                count += 1
        return count
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for num in range(num1, num2 + 1):
            ans += self.waviness(num)
        return ans

