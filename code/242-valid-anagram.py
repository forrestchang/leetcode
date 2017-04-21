class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        set_s = list(set(s))
        set_t = list(set(t))
        if len(set_s) == len(set_t):
            for c in set_s:
                if s.count(c) != t.count(c):
                    return False
            return True
        return False
