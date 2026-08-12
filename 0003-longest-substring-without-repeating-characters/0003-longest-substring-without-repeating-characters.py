class Solution:
    def lengthOfLongestSubstring(self, s):
        ans = ""
        max_len = 0

        for ch in s:
            if ch in ans:
                ans = ans[ans.index(ch) + 1:]

            ans += ch

            if len(ans) > max_len:
                max_len = len(ans)

        return max_len