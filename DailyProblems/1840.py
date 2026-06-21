class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions_d={}
        val_list=[[0,0]]
        for key,value in restrictions:
            restrictions_d[str(key)]=value
        for k in range(1,n):
            if str(k) in restrictions_d:
                max_heigh=restrictions_d.get(str(k))
                value=val_list[-1][1]
                if max_heigh <= value:
                    value=+1
                else:
                    value = max_heigh-1
                val_list.append([k,value])
            else:
                # min_heigh=val_list[-1][1]
                value =val_list[-1][1]+1
                val_list.append([k,value])
        return max([i[1] for i in val_list])

# if __name__ == '__main__':
#     s=Solution()
#     max_heigh=s.maxBuilding(n=5,restrictions=[[2,1],[4,1]])
#     print(max_heigh)

