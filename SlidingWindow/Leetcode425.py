class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_d={}
        max_f=0
        l=0
        res=0

        for r in range(len(s)):
            s_d[s[r]]=1+s_d.get(s[r],0)
            max_f=max(max_f,s_d[s[r]])

            while ( r - l + 1)-max_f > k :
                s_d[s[l]] -= 1
                l += 1
            res= max( r - l + 1, res)
        return res




# if __name__ == '__main__':
#      s= Solution()
#      cu=s.characterReplacement(s="AABABBA",k=2)
#      print(cu)