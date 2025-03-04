class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize two pointers:
        # 'i' starts from the beginning
        # 'j' starts from the end of the string
        i = 0
        j = len(s) - 1

        while i < j:
            # Skip non-alphanumeric characters on the left pointer
            if not s[i].isalnum():
                i += 1
                continue

            # Skip non-alphanumeric characters on the right pointer
            if not s[j].isalnum():
                j -= 1
                # * The continue statement is important here because it skips the remaining code
                #   in the current loop iteration and immediately moves to the next iteration.
                continue

            # Compare characters in a case-insensitive manner
            if s[i].lower() != s[j].lower():
                return False

            # Move both pointers closer to the center if it's a valid match 
            i += 1
            j -= 1

        return True

