```
https://leetcode.com/problems/two-sum/description/

* algorithms
* Easy (43.54%)
* Total Accepted:    1.7M
* Total Submissions: 3.9M
* Testcase Example:  '[2,7,11,15]\n9'

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,a in enumerate(nums):
                b = target-a
                if b in nums:
                    j = nums.index(b)
                    if i!=j:
                        return [i,j]
                    
