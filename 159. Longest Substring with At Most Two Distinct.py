#159. Longest Substring with At Most Two Distinct Characters

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        dic = {}
        start = 0
        larg = 0 
        for i in range(len(s)):
            if len(dic) == 2 and s[i] not in dic:
                dic[s[i]] = i
                start = min(dic.values()) + 1
                self.help(dic)
            dic[s[i]] = i
            larg = max(larg, i - start + 1)
            
        return larg 
    

        
    def help(self, dic):
        lowest = min(dic.values())
        for k, pos in dic.items():
            if pos == lowest:
                char = k
        dic.pop(char)