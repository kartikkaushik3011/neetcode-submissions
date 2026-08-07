class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        tcount,scount={},{}
        l=0
        res,resLen=[-1,-1],float("inf")
        for c in t:
            tcount[c]=1+tcount.get(c,0)
        have,need=0,len(tcount)
        for r in range(len(s)):
            scount[s[r]]=1+scount.get(s[r],0)
            if s[r] in tcount and scount[s[r]]==tcount[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                scount[s[l]]-=1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if resLen!=float("inf") else ""