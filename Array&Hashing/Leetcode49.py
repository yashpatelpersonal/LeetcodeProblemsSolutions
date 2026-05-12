class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main={}
        for key  in strs:
            words = "".join(sorted(key))
            if words not in  main:
                main[words]=[]
            main[words].append(key)
        return sorted(main.values())

if __name__ == '__main__':
    s=Solution()
    s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])