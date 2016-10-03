class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums.sort()
        for _ in nums:
            try:
                if nums[i+1]-nums[i] == 0:
                    i += 2
            except IndexError:
                return nums[-1]
        return nums[i]