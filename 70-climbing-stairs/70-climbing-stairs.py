class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        a, b= 1, 2
        temp = 0
        for i in range(3, n+1):
            temp = a+b
            a = b
            b = temp
        return temp
            