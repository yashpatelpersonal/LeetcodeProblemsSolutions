class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        max_c=0
        for i in range(len(height)):
            right=i+1
            while  right < len(height)   :
                cal=min(height[i],height[right])
                extra=cal * (right - start)
                max_c =  extra if extra > max_c else max_c
                right+=1
            start=start+1
        return max_c #if  max(max_area)<= 469000 else 0


# if __name__ == '__main__':
#     s= Solution()
#     return_=s.maxArea(height=[1,1])
#     print(return_)