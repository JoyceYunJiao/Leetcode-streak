class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        #create hashmaps to store the combination 
        p_to_s = {}
        s_to_p = {}

        #split the string 
        s = s.split()

        #if the pattern doesn't match, return False
        if len(pattern) != len(s):
            return False

        for p, w in zip(pattern, s):
            #if pattern doesn't match word return False 
            if p in p_to_s and p_to_s[p] != w:
                return False

            #if word doesn't match work return False     
            if w in s_to_p and s_to_p[w] != p:
                return False
                
            #if the pattern or word is not in hashmap yet, add them
            p_to_s[p] = w
            s_to_p[w] = p
        return True

