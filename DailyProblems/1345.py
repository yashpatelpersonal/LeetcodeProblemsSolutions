
class Solution:
    def __init__(self):
        self.current=0
    def bsf(self,arr:List[int],start,current_in):
        if current_in <= 0 or  current_in == len(arr) - 1 or start<=0:
            return self.current
        if start in arr:
            index_f=arr.index(start)
            arr[index_f]*=-1
            self.current+=1
            self.bsf(arr=arr,start=start,current_in=current_in)
        if start not in arr:
            index_f=current_in+1
            self.current+=1
            arr[index_f]*=-1
            self.bsf(arr=arr,start=arr[index_f],current_in=index_f)

    def minJumps(self, arr: List[int]) -> int:
        start=arr[0]
        arr[0]*=-1
        return self.bsf(arr=arr,current_in=0,start=start)


if __name__ == '__main__':
    s= Solution()
    c=s.minJumps(arr=[100,-23,-23,404,100,23,23,23,3,404])
    print(c)