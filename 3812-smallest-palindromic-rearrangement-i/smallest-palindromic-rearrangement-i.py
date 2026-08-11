class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # get the word in terms of half the word.
        # sort the half word, and copy it

        l = len(s)
        
        middle = int(l/2) # the end pointer (non-inclusive)
        midChar = None

        if l % 2 == 1:
            midChar = s[middle]
        
        halfWord = s[:middle]
        print(halfWord)
        halfWord = "".join(sorted(halfWord))

        ans = halfWord
        if midChar:
            ans += midChar
        ans += halfWord[::-1]
        return ans


        