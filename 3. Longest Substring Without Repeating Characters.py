# my solution
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        larg = 0
        star = 0
        end = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
                end = i
                if (end-star+1) > larg:
                    larg = (end-star+1)
            else:
                if dic[s[i]] >= star:
                    star = dic[s[i]] + 1
                    dic[s[i]] = i
                    end = i
                    if (end-star+1) > larg:
                        larg = (end-star+1)
                else:
                    dic[s[i]] = i
                    end = i
                    if (end-star+1) > larg:
                        larg = (end-star+1)
        return larg

#other's
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength