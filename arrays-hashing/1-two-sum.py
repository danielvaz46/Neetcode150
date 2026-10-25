# LeetCode 1. Two Sum (NeetCode 150)
# https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Pattern: arrays-hashing
# Time: O(n)  Space: O(n)
# Insight:
#   - enumerate(nums) gives index and value together, instead of
#     for i in range(len(nums)) with nums[i].
#   - No special-casing the first element: start with an empty dict. The first number
#     finds nothing and gets stored, so there's no need to seed it with nums[0]: 0.
#   - Why a partial dict works: when we reach index i, seen only holds indices before i.
#     For any valid pair (j, i) with j < i, j is already stored when we reach i,
#     so the pair is found at its later element.
#   - Checking before inserting means an element can't pair with itself, while
#     duplicates still work ([3, 3], target 6: the first 3 is stored before the
#     second is checked).

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
