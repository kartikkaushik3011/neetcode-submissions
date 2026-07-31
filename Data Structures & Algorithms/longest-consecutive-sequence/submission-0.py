class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        set1=set(nums)
        for n in nums:
            length=0
            if(n+1) not in set1:
                while(n-length)in set1:
                    length+=1
            res=max(res,length)
        return res