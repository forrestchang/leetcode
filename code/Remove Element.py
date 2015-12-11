class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        back = -1
        front = 0
        for front in range(0, len(nums)):
            if val != nums[front]:
                nums[back + 1] = nums[front]
                back += 1
        return back + 1
