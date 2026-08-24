class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = len(s)
        stri = list()
        n = 0 
        left = 0 
        for right in range(l):
            while s[right] in stri:
                stri.remove(s[left])
                left+=1
            stri.append(s[right])
            n = max(n, right -left + 1)
        
        return n 



            