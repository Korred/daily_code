class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 2147483647 = 2^31 - 1 = max-int size on 32-Bit systems
        # however in Python3 int is simply converted to long so max_int size does not matter
        
        s = str(x)

        if s[0] == '-':
            s = int(s[0] + s[1:][::-1])
        else:
            s = int(s[::-1])
        
        if s >= -2147483648 and s <= 2147483647:
            return s
        else: 
            return 0 

# Example use:
a = 123456789
print(a, Solution().reverse(a))