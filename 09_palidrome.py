class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = x
        if x < 0:
            return False
        r = 0
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        if y == r:
            return True 
            