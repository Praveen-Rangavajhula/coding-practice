class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Approach 1: 
        # Probably the simplest approach, we sort both of them
        # and see if they match exactly

        # return sorted(s) == sorted(t)

        # Approach 2: 
        # Brute force, probably not the best way to go about this
        # Remove matching pairs until string is empty (if True)
        # As expected we get TLE. 

        # chars_s = list(s)
        # chars_t = list(t)

        # for char_s in chars_s.copy():
        #     for char_t in chars_t.copy():
        #         if char_s == char_t:
        #             if char_s not in chars_s or char_t not in chars_t:
        #                 return False
        #             chars_s.remove(char_s)
        #             chars_t.remove(char_t)

        # return not chars_s and not chars_t

        # Approach 3: 
        # This is the first idea I got
        # We can try having a hashmap to account for each time
        # a character appears 

        if len(s) != len(t):
            return False

        hashmap = {}

        for char_s, char_t in zip(s, t):
            hashmap[char_s] = hashmap.get(char_s, 0) + 1
            hashmap[char_t] = hashmap.get(char_t, 0) - 1

        return all(value == 0 for value in hashmap.values())




