class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return None
        return s[::-1]

if __name__ == '__main__':
    assert Solution().reverseString('hello world') == 'dlrow olleh'
    assert Solution().reverseString('') == None
    print('All test cases passed!')
