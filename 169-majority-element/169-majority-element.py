class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        Hash = Counter(nums)
        for i, val in Hash.items():
            if val > len(nums) / 2:
                return i