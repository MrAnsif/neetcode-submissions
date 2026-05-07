class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_s = s.replace(" ", "").lower()
        res = ""
        for i in trimmed_s:
            if i.isalnum():
                res += i
        return res == res[::-1]