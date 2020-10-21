class Solution:
    def grayCode(self, n):
        """
        Calculates a valid gray code sequence given a non-negative integer n 
        that represents the total number of bits in the code.

        Args:
            n: int
                Total number of bits in code

        Returns:
            List[int]
                A valid gray code sequence of length 2**n

        Raises:
            KeyError: Raises an exception.
        """

        if n == 0: return [0]

        if n == 1: return [0, 1]

        # get previous grayCode list
        prv = self.grayCode(n-1)

        # add '0' to each binary representation of previous grayCode list and convert back to int
        left = [int('0' + format(e, '0{}b'.format(n-1)), 2) for e in prv]

        # add '1' to each binary representation or reversed previous grayCode list and convert back to int
        right = [int('1' + format(e, '0{}b'.format(n-1)), 2) for e in reversed(prv)]

        # and then return joined list
        return left + right

# Example use:
n = 3
print(n, ":", Solution().grayCode(n))