import string

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])


if __name__ == '__main__':
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("cc") == -1
    assert Solution().firstUniqChar("loveleetcode") == 2
