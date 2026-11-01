class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Approach 1: Brute Force

        pre = strs[0]

        for i in range(1, len(strs)):
            count = 0
            word = strs[i]

            for i in range(min(len(pre), len(word))):
                if pre[i] == word[i]:
                    count += 1
                else: 
                    break

            pre = pre[:count]

        return pre
