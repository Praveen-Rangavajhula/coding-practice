class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Approach 1: 
        # If we want to brute force this, we can have a char counter. 
        # And since we only have 26 possible options, we can pick 
        # each of the strings and count their char frequencies, but then
        # how would you store them? That's expensive 
        #
        # Firstly, anagrams. Let's see their properties:
        # 1. Same characters (exactly)
        # 2. This implies same length
        # 3. This also implies, when sorted they will end up in the same bin.
        # 
        # In which case, we can have a map of the sorted to the original
        # indices, and then put them in bins, and return the final list
        # as the original indices. Let's try that.

        # While doing this, i just realized that dictionaries can't have 
        # duplicate keys, so we might need to switch to tuples. 

        sorted_words = sorted(
            [(''.join(sorted(word)), i) for i, word in enumerate(strs)]
        )
        
        # Now we need to figure out how to bin them 
        # Method 1: Brute force 

        _, first_idx = sorted_words[0]

        idxs = {first_idx}
        anagrams = []

        for i in range(len(strs) - 1):
            cur_word, cur_idx = sorted_words[i]
            next_word, next_idx = sorted_words[i+1]

            if cur_word == next_word: 
                idxs.update((cur_idx, next_idx))
            else: 
                idxs.add(cur_idx)
                anagrams.append([strs[i] for i in idxs])
                idxs.clear()

        _, last_idx = sorted_words[-1]
        idxs.add(last_idx)
        anagrams.append([strs[i] for i in idxs])
        idxs.clear()

        return anagrams






        
