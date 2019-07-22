class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def _check(alist):
        #     max_num = max(alist)
        #     for elem in alist:
        #         if elem != max_num:
        #             return False
        #     return True
        # count = 0
        # while not _check(nums):
        #     count += 1
        #     max_index = nums.index(max(nums))
        #     for i in range(len(nums)):
        #         if i != max_index:
        #             nums[i] += 1
        # return count
        min_num = min(nums)
        res = 0
        for n in nums:
            res += n - min_num
        return res


if __name__ == '__main__':
    assert Solution().minMoves([1, 2, 3]) == 3
    assert Solution().minMoves([1, 5, 2]) == 5
