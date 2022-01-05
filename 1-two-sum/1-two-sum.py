class Solution(object):
    def twoSum(self, nums, target):
        table = {}
        # x + y = target
        # target - num in table
        for i, val in enumerate(nums):
            if target - val in table:
                return table[target - val], i
            table[val] = i
        return None