class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def _breakup(complex_number):
            split = complex_number.split('+')
            x, y = split[0], split[1].rstrip('i')
            return (int(x), int(y))
        x1, y1 = _breakup(a)
        x2, y2 = _breakup(b)
        real = x1 * x2 - y1 * y2
        virtual = x1 * y2 + y1 * x2
        return '{real}+{virtual}i'.format(real=real, virtual=virtual)


if __name__ == '__main__':
    assert Solution().complexNumberMultiply('1+1i', '1+1i') == '0+2i'
    assert Solution().complexNumberMultiply('1+-1i', '1+-1i') == '0+-2i'
