class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        tcount = {}
        for char in t:
            tcount[char] = 1 + tcount.get(char, 0)

        scount = {}
        have, need = 0, len(tcount)

        # Track (window_length, left_index, right_index)
        res = float("inf"), 0, 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            scount[char] = 1 + scount.get(char, 0)

            # If the current character count matches the required count in t
            if char in tcount and scount[char] == tcount[char]:
                have += 1

            # Try to shrink the window from the left while it remains valid
            while have == need:
                # Update our minimum window result
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)

                # Pop from the left of our window
                scount[s[l]] -= 1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1

        length, l, r = res
        return s[l : r + 1] if length != float("inf") else ""