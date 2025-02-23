class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

    # The key to solving this problem is recognizing that in those six certain cases, 
    # a smaller Roman numeral appears before a larger one, indicating subtraction.
    # To handle this, we subtract the value of the first numeral in the pair  
    # and add the value of the last numeral separately.  
    # This approach effectively accounts for both subtraction and addition cases. 

        roman_to_int = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        num = 0
        # Treat the string 's' as an array and iterate until the second-to-last character
        for i in range(len(s)-1):
            # Subtract if the current numeral is smaller than the next one 
            # (indicating a subtraction case)
            if roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                num = num - roman_to_int[s[i]]
            # Otherwise, add the numeral's value
            else:
                num = num + roman_to_int[s[i]]
                
        # Add the last numeral since the loop only iterates up to the second-to-last index 
        num = num + roman_to_int[s[-1]]
        return num

        
