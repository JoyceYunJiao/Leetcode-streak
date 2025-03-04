class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Remove non-alphanumeric characters and convert to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        #Reverse the cleaned string
        backward = ''.join(reversed(s))

        #Compare the original and reversed strings
        return s == backward
