class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s = sorted(s)
        t_s = sorted(t)
        return True if s_s == t_s else False