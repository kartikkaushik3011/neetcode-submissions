class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1=dict()
        dict2=dict()
        for i in s:
            dict1[i]=1+dict1.get(i,0)
        for i in t:
            dict2[i]=1+dict2.get(i,0)
        return dict1==dict2