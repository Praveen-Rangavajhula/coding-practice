class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Approach 1: Sorting 

        d = defaultdict(list)

        for word in strs: 
            d[''.join(sorted(word))].append(word)

        anagrams = list(d.values())
        
        return anagrams

