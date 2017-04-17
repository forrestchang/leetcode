class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _check(nums):
            for num in nums[1:]:
                if num != nums[0]:
                    return False
            return True
        count = 0
        while _check(nums) is False:
            max_num = max(nums)
            nums = [num + 1 for num in nums if num != max_num] + [max_num]
            count += 1
        return count


if __name__ == '__main__':
    print(Solution().minMoves([1, 2, 3]))
    assert Solution().minMoves([1, 2, 3]) == 3
    assert Solution().minMoves([1, 5, 2]) == 5
