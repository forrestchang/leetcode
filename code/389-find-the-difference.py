class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # dic = {}
        # for c in s:
        #     dic[c] = dic.get(c, 0) + 1
        # for c in t:
        #     if dic.get(c, 0) == 0:
        #         return c
        #     else:
        #         dic[c] -= 1
        code = 0
        for c in s + t:
            code ^= ord(c)
        return chr(code)


if __name__ == '__main__':
    assert Solution().findTheDifference('abcd', 'abcde') == 'e'
    assert Solution().findTheDifference('abcd', 'abcdg') == 'g'
    assert Solution().findTheDifference('abcd', 'abcdc') == 'c'
    assert Solution().findTheDifference('a', 'aa') == 'a'
