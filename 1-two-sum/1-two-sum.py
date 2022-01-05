class Solution(object):
    def twoSum(self, nums, target):
        table = {}
        for i, val in enumerate(nums):
            remain = target - val
            if remain in table:
                return table[remain], i
            table[val] = i
            
        return None
     