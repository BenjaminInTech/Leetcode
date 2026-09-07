class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        leng = 0
        l = r = 0
        curr_sub = []

        while r < len(s):
            if s[r] in curr_sub:
                curr_sub.remove(s[l])
                l += 1
                leng -= 1
            else:
                curr_sub.append(s[r])
                r += 1
                leng += 1
                if leng > mx:
                    mx = leng

        return mx
        