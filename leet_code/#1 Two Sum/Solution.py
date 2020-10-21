class Solution:

    # Bruteforce approach
    def twoSumBrute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num_a in enumerate(nums):
            for j, num_b in enumerate(nums[i+1:]):
                if num_a + num_b == target:
                    return [i, j+i+1]

    # HashMap/dict() approach
    def twoSumDict(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        checked = {}
        for i, num in enumerate(nums):
            if num in checked:
                return [checked[num], i]

            diff = target - num

            if diff not in checked:
                checked[diff] = i


# Example use:
nums = [3, 2, 4, 12, 6, 125, 126, -4, -2]
target = 123
print(Solution.twoSumDict(nums, target))
