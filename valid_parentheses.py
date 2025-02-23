class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The key of this problem is to use the hashmap and stack data structure.
        # As first in last out as the property of the stack
        # We can check if the closing bracket matches the last open bracket that was pushed onto the stack.
        bracket_pairs = {"(": ")", "{": "}", "[": "]"}

        # Initialize an empty stack to keep track of open brackets.
        stack = []

        # Iterate through each character in the string.
        for element in s:
            # If the character is an open bracket, push it onto the stack.
            if element in bracket_pairs.keys():
                stack.append(element)
            # If the character is a closing bracket...
            elif element in bracket_pairs.values():
                # Return False if the stack is empty or if the top of the stack doesn't match the closing bracket.
                if not stack or bracket_pairs[stack[-1]] != element:
                    return False
                # Remove the matching open bracket from the stack.
                stack.pop()
                
        # Return True only if all opening brackets have been matched 
        #(i.e., the stack is empty).

        #return len(stack) == 0
        return not stack

