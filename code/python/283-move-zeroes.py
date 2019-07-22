class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # i, j = 0, 1
        # while j < len(nums):
        #     if nums[i] == 0:
        #         if nums[j] != 0:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #             j += 1
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == '__main__':
    num1 = [0, 1, 0, 3, 12]
    num2 = [1]
    num3 = [0]
    num4 = [1, 2, 3, 4, 0]
    num5 = [0, 0, 0, 1, 2, 3]
    Solution().moveZeroes(num1)
    Solution().moveZeroes(num2)
    Solution().moveZeroes(num3)
    Solution().moveZeroes(num4)
    Solution().moveZeroes(num5)
    assert num1 == [1, 3, 12, 0, 0]
    assert num2 == [1]
    assert num3 == [0]
    assert num4 == [1, 2, 3, 4, 0]
    assert num5 == [1, 2, 3, 0, 0, 0]
