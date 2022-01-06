class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort() # sort the string according to a-z
        end = min((len(strs[0])), len(strs[len(strs)-1]))
        
        i = 0
        while i<end and strs[0][i] == strs[len(strs)-1][i]:
            i += 1
        
        pre = strs[0][0: i]
        return pre