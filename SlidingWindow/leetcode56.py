class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        if len(intervals)<=1:
            return intervals
        result=[]
        start,end=intervals[0][0],intervals[0][1]
        for k in range(1,len(intervals)):
            if end >= intervals[k][0] and end <= intervals[k][1] :
                end=max(intervals[k][1],end)
                start=min(start,intervals[k][0])
                result.append([start,end])
            elif len(intervals) == 2:
                result.append([start,end])
                result.append([intervals[k][0],intervals[k][1]])
            else :
                if intervals[k][0] <= start and intervals[k][1]>=end:
                    start=intervals[k][0]
                    end=intervals[k][1]
                result.append([start,end])
        return result
        # return res


# if __name__ == '__main__':
#     s= Solution()
#     result=s.merge(intervals=[[1,6],[2,4],[8,10],[15,18]])
#     print(result)