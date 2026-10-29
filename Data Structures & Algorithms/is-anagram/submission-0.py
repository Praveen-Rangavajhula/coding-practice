class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Approach 1: 
        # Probably the simplest approach, we sort both of them
        # and see if they match exactly

        return sorted(s) == sorted(t)
