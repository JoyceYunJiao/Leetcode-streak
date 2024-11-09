class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        both solutions has time complexity O(n), space complexityO(n)
        there is a better solution that has space complexity O(1)
        my first solution: 
        converted_int = str(x)
        
        converted_int = converted_int[::-1]

        return converted_int == converted_int[::-1]
        """
        if x < 0: 
            return False
        
        rev = 0
        res = x
        while res != 0:
            digit = res % 10
            rev = 10*rev + digit
            res = res / 10
        return rev == x
                

