class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        columns = len(nums[0])
        if r > rows or c > columns:
            return nums
        row = []
        new = []
        return 0


if __name__ == '__main__':
    nums = [[1, 2], [3, 4]]
    assert Solution().matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
