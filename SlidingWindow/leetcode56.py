class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda i : i[0] )       # return res
        return_=[intervals[0]]
        for start,end in intervals[1:]:
            last_val=return_[-1][1]
            if start <= last_val:
                return_[-1][1]=max(last_val,end)
            else:
                return_.append([start,end])
        return return_



# if __name__ == '__main__':
#     s= Solution()
#     result=s.merge(intervals=[[1,6],[2,4],[8,10],[15,18]])
#     print(result)