class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each word, make their char frqs. map frq -> word to group them
        # to represent a char frq, we can just get an array of 26, each reps a char

        frqMap = defaultdict(list) # frq arr -> [list of words]

        for s in strs:
            frqs = [0] * 26
            for c in s:
                frqs[ord(c) - ord('a')] += 1
            frqMap[tuple(frqs)].append(s)
        
        # get all the groups

        return list(frqMap.values())
            