class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort_nums = sorted(nums, reverse=True)
        dic = {}
        for i, num in enumerate(sort_nums, 1):
            # All the scores of athletes are guaranteed to be unique.
            dic[num] = i
        ans = []
        for num in nums:
            if dic[num] == 1:
                ans.append('Gold Medal')
            elif dic[num] == 2:
                ans.append('Silver Medal')
            elif dic[num] == 3:
                ans.append('Bronze Medal')
            else:
                ans.append(str(dic[num]))
        return ans


if __name__ == '__main__':
    assert Solution().findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert Solution().findRelativeRanks([10,3,8,9,4]) == ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
