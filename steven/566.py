class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        res = [[0] * c for i in range(r)]
        i = 0
        j = 0
        for row in nums:
            for elem in row:
                res[i][j] = elem
                j += 1
                if j >= c:
                    j = 0;
                    i += 1
        return res

