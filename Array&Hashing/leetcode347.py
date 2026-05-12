#top topKFrequent
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i not in a:
                a[i]= 1
            else:
                a[i]+=1
        max_v=sorted(a.values(),reverse=True)[:k]
        top=[]
        for i in a:
            if a.get(i) in max_v:
                top.append(i)
        return top


if __name__ == '__main__':
    s=Solution()
    val=s.topKFrequent(nums=[1,1,1,2,2,3],k=2)
    print(val)