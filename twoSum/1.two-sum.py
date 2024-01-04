#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(0, len(nums)):
            for second_num in range(0, len(nums)):
                if (nums[num] + nums[second_num] == target) and (num != second_num):
                    return [num, second_num]
# @lc code=end
