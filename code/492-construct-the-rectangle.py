class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        begin = int(sqrt(area))
        for length in xrange(begin, area + 1):
            if area % length == 0:
                if length >= area // length:
                    return [length, area // length]


if __name__ == '__main__':
    assert Solution().constructRectangle(4) == [2, 2]
