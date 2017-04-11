class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        le = len(bin(num)) - 2
        shift = 1 << 32
        complemt = ~num
        result = bin(shift + complemt)[-le:]
        return int(result, 2)

if __name__ == '__main__':
    assert Solution().findComplement(5) == 2
    assert Solution().findComplement(1) == 0
