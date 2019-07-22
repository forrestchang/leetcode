class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # This problem is fucked.
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == '__main__':
    assert Solution().findLUSlength('aba', 'cdc') == 3
