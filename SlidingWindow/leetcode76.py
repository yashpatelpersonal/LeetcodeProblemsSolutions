class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="": return ""
        if len(s) < len(t): return ""
        if s == t: return t
        count_t,win_t={},{}
        for i in t:
            count_t[i] = 1 + count_t.get(i,0)
        have, need = 0, len(count_t)
        res , res_l =[-1,-1], float("infinity")
        r= 0
        for l in range(len(s)):
            c = s[l]
            win_t[c]= 1 + win_t.get(c,0)
            if c in count_t and win_t[c] == count_t[c]:
                have+=1
            while have == need:
                if ( l - r + 1 ) < res_l:
                    res=[r , l ]
                    res_l=(l- r + 1)
                win_t[s[r]]-=1
                if s[r] in count_t and win_t[s[r]] < count_t[s[r]]:
                    have -=1
                r+=1
        r,l=res
        # print(r,l)
        return s[r:l+1] if res_l != float('infinity') else ""



# if __name__ == '__main__':
#     s= Solution()
#     res=s.minWindow(s="ADOBECODEBANC",t="ABC")
#     print(res)