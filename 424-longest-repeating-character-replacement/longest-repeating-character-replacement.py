class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # for the window, keep track of all the char counts. you keep track of the max the whole time.
        # the window stays valid as long as length <= maxfrq + k
        # keep extending window 1 if valid. when invalid, keep removing from front until valid

        frqs = [0] * 26
        l, r = 0, 0 # including ind l, including ind r
        ans = 0

        while r < len(s):
            # include ind r
            addC = s[r]
            frqs[ord(addC)-ord('A')] += 1

            while r-l+1 > max(frqs) + k: # window became invalid, keep removing from the back
                removeC = s[l]
                frqs[ord(removeC)-ord('A')] -= 1
                l += 1
            
            # window is confirmed valid
            ans = max(ans, r-l+1)
            # move r to include the next one
            r += 1
        
        return ans

