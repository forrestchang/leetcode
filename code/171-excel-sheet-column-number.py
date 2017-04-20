import string

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        def _to_26(c):
            return ord(c) - ord('A') + 1
        num = 0
        for i in range(len(s)):
            num += _to_26(s[-(i+1)]) * 26 ** i
        return num


if __name__ == '__main__':
    assert Solution().titleToNumber('AA') == 27
