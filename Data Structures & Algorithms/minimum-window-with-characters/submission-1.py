class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        tcount = {}
        for char in t:
            tcount[char] = 1 + tcount.get(char, 0)

        scount = {}
        have, need = 0, len(tcount)
        res = float("inf"), 0, 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            scount[char] = 1 + scount.get(char, 0)
            if char in tcount and scount[char] == tcount[char]:
                have += 1
            while have == need:
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)
                scount[s[l]] -= 1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1

        length, l, r = res
        return s[l : r + 1] if length != float("inf") else ""