# LeetCode 217. Contains Duplicate (NeetCode 150)
# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Pattern: arrays-hashing
# Time: O(n)  Space: O(n)
# Insight: A set drops duplicates, so if it's smaller than the input, something repeated.
#          Alternative: loop with a "seen" set and return True on the first repeat.
#          Same big-O, but it can exit early when a duplicate appears near the front.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
