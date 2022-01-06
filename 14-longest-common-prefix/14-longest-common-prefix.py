class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        
        strs.sort() # sort the string according to a-z
        end = min((len(strs[0])), len(strs[-1]))   # reduce time
        
        i = 0
        while i < end and strs[0][i] == strs[-1][i]: 
        # compare the first and last string since if there's a matching prefix between first and last string,               strings in b/w will contain that prefix too
            i += 1
        
        pre = strs[0][0: i]
        return pre