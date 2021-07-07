'''
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

class Solution(object):
	def twoSum(self, nums, target):
		dict = {}

		for index, val in enumerate(nums):
			diff = target - val
			if diff in dict:
				return [dict[diff],index]
			else:
				dict[val] = index

# Space: O(N)
# Time: O(N)
nums = [2,7,8,11]
target = 9
y = Solution()
print(y.twoSum(nums,target))
