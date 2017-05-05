class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        nums.sort()
        for i in xrange(0, len(nums), 2):
            s += min(nums[i], nums[i + 1])
        return s
