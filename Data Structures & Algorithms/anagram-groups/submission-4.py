class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Approach 2: Hashing

        result = defaultdict(list)

        for word in strs: 
            counts = [0] * 26

            for w in word: 
                counts[ord(w) - ord('a')] += 1

            result[tuple(counts)].append(word)

        return list(result.values())
