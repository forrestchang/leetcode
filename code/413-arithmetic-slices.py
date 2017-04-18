class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def _check(sublist):
            for i in range(len(sublist) - 2):
                if sublist[i+1] - sublist[i] != sublist[i+2] - sublist[i+1]:
                    return False
            return True
        count = 0
        for shift in range(3, len(A) + 1):
            begin = 0
            end = begin + shift
            while end <= len(A):
                if _check(A[begin:end]):
                    count += 1
                begin += 1
                end += 1
        return count


if __name__ == '__main__':
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3
