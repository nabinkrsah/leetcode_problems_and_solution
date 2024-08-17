"""Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 
    """



class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math

        if c < 0:
            return False

        a = 0
        b = int(math.sqrt(c))
        
        while a <= b:
            current_sum = a * a + b * b
            if current_sum == c:
                return True
            elif current_sum < c:
                a += 1
            else:
                b -= 1
                
        return False
