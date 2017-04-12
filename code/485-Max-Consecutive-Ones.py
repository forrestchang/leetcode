class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        counts = []
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                counts.append(count)
                count = 0
        counts.append(count)
        return max(counts)


if __name__ == '__main__':
    assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
    assert Solution().findMaxConsecutiveOnes([0, 0]) == 0
    assert Solution().findMaxConsecutiveOnes([1]) == 1
    assert Solution().findMaxConsecutiveOnes([0]) == 0
    assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1, 1, 1, 1, 0, 0]) == 6

