class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        xor = x ^ y
        while xor:
            distance += xor & 1
            xor >>= 1
        return distance
    
    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        xor = x ^ y
        while xor > 0:
            distance += xor % 2
            xor /= 2
        return distance
