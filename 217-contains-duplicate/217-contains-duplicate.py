class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for i in nums:
            if c[i] > 1:
                return True
        return False
        