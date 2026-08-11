class Solution:
    def minimumPushes(self, word: str) -> int:
        # each number 2-9 can be mapped to a character
        # 8 -> 1 push, 8 -> 2 push, ...

        # greedy: maximize the uses of lower push mappings: higher frqs chars get lower push

        # get the unique chars and the frq of each. then slot each one into a mapping: 8 1 push, 8 2 push, 8 3 push, 1 4 push

        frqs = defaultdict(int)
        for c in word:
            frqs[c] += 1
        
        frqsOrder = sorted(list(frqs.values()), reverse=True)

        mapLvlCount = 0 # this is the 1, 2 ... 8, 1 ...
        lvlPushes = 1
        ans = 0

        for i in range(len(frqs)):
            if mapLvlCount == 8: # move to the next lvl
                lvlPushes += 1
                mapLvlCount = 0
            
            ans += frqsOrder[i] * lvlPushes

            mapLvlCount += 1
        
        return ans
            