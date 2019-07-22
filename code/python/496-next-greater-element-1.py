class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in findNums:
            index = nums.index(num)
            li = [n for n in nums[index+1:] if n > num]
            if li:
                result.append(li[0])
            else:
                result.append(-1)
        return result

if __name__ == '__main__':
    # assert Solution().nextGreaterElement([4,1,2], [1,3,4,2]) == [-1, 3, -1]
    # assert Solution().nextGreaterElement([2,4], [1,2,3,4]) == [3, -1]
    print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
    print(Solution().nextGreaterElement([2,4], [1,2,3,4]))
