class Solution:
    from collections import Counter
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): #save space 
            nums1, nums2 = nums2, nums1
        c1 = Counter(nums1)
        result = []
        for i in nums2:
            if c1[i] > 0: # check if counter includes the no
                result.append(i)    # if c1[i]=0, then move on next i in nums2 
                c1[i] -= 1
        return result