class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                sum += nums[i]
        return sum

if __name__ == '__main__':
    assert Solution().arrayPairSum([1, 4, 3, 2]) == 4
