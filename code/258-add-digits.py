from functools import reduce

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            print(num)
            return num
        else:
           return self.addDigits(reduce(lambda a, b: a + b, [int(c) for c in str(num)]))


if __name__ == '__main__':
    # print(Solution().addDigits(38))
    assert Solution().addDigits(38) == 2
    # print(reduce(lambda a, b: a+b, [int(c) for c in str(11)]))
