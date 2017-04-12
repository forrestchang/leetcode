class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result


if __name__ == '__main__':
    assert Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
