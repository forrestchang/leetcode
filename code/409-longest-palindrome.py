class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        set_s = set(s)
        exist_one = False
        count = 0
        for c in set_s:
            if s.count(c) % 2 == 0:
                count += s.count(c)
            else:
                count += s.count(c) - 1
                exist_one = True
        if exist_one:
            count += 1
        return count


if __name__ == '__main__':
    assert Solution().longestPalindrome('abccccdd') == 7
