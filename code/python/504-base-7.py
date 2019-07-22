class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # if num < 0:
        #     return '-' + self.convertToBase7(-num)
        # if num < 7:
        #     return str(num)
        # return self.convertToBase7(num // 7) + str(num % 7)
        def _convert(num):
            ans = ''
            while num:
                ans = str(num % 7) + ans
                num = num // 7
            return ans
        if num < 0:
            return '-' + _convert(-num)
        if num == 0:
            return '0'
        else:
            return _convert(num)
