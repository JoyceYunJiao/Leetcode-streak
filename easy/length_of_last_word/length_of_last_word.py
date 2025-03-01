class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #split the string
        s = s.split()
        #get the last word of s
        word = s[-1]
        #print out the information
        #note that + operator requires the same data type, so we need to convert integer to the string 
        print("The last word is " + word + " with length " + str(len(word)) + ".")
        return len(word)

