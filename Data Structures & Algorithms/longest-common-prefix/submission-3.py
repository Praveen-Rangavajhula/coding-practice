class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Approach 2: Sorting

        strs = sorted(strs)

        first_word = strs[0]
        last_word = strs[-1]

        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] != last_word[i]:
                return first_word[:i]

        return first_word
