# Runtime comparison using timeit-module

```python
import timeit

setup = '''
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


nums = [3, 2, 4, 12, 6, 125, 126, -4, -2]
target = 6
a = Solution()
'''

print("Bruteforce:", min(timeit.Timer(stmt="a.twoSumBrute(nums, target)", setup=setup).repeat(7, 10000)))
print("Hashmap/Dict():", min(timeit.Timer(stmt="a.twoSumDict(nums, target)", setup=setup).repeat(7, 10000)))
```

##### Results:
```
Brutforce: 0.06600504951714442
Hashmap/Dict: 0.024372493051178612
```
