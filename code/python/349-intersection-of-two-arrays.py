class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for n in nums1:
        #     if n in nums2:
        #         if n not in ans:
        #             ans.append(n)
        # return ans
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
