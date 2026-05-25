#Problem :Given a list of intervals, merge all intervals that overlap and return the merged list.
# Inputs : [[1,3],[2,6],[8,10],[15,18]]
#Output : [[1,6],[8,10],[15,18]]


class Solution:
    def merge(self,num):
        num.sort(key =lambda i : i[0] )       # return res
        return_list=[[num[0][0],num[0][1]]]
        for key in range(1,len(num)):
            if num[key][0]  <= return_list[-1][1]:
                return_list[-1][1]=max(num[key][1],return_list[-1][1])
            else:
             return_list.append([num[key][0],num[key][1]])
        return return_list

if __name__ == '__main__':
    s=Solution()
    merge_list=s.merge([[1,3],[2,6],[8,10],[15,18]])
    print("After Merging Intervals",merge_list)



