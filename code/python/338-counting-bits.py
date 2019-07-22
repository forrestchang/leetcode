class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
        def _bin(num):
            s = []
            while num > 0:
                s.append('0' if num % 2 == 0 else '1')
                num = num // 2
            return ''.join(s)
        def _count_1(s):
            count = 0
            for c in s:
                if c == '1':
                    count += 1
            return count
        ans = []
        for i in range(num + 1):
            ans.append(_count_1(_bin(i)))
        return ans


if __name__ == '__main__':
    assert Solution().countBits(5) == [0,1,1,2,1,2]
