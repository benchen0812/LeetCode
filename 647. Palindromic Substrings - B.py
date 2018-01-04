# 647. Palindromic Substrings

class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0 
        
        for center in range (2*N -1):
            l = center /2
            r = l + center % 2
            
            while l >= 0 and r < N and S[l] == S[r]:
                ans += 1
                l -= 1
                r += 1
                
        return ans 