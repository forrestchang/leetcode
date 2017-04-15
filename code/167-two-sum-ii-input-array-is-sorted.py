class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums = sorted(list(set(numbers)))
        # for num1 in nums:
        #     for num2 in nums:
        #         if num1 + num2 == target:
        #             if num1 != num2:
        #                 return [numbers.index(num1) + 1, numbers.index(num2) + 1]
        #             else:
        #                 return [numbers.index(num1) + 1, numbers.index(num1) + 2]
        front, end = 0, len(numbers) - 1
        while numbers[front] + numbers[end] != target:
            if numbers[front] + numbers[end] < target:
                front += 1
            else:
                end -= 1
        return [front + 1, end + 1]


if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
    assert Solution().twoSum([0, 0, 3, 4], 0) == [1, 2]
