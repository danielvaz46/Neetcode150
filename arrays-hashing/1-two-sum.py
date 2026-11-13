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
# Interview Q&A:
#   Q: What are the time and space complexities, and what is the trade-off?
#   A: O(n) time and O(n) space for the dict. Brute force flips it: O(n^2) time, O(1) space.
#   Q: What if the array is sorted?
#   A: Use two pointers for O(n) time and O(1) space (see 167).
#   Q: What if you must return every valid pair, not just one?
#   A: Don't return early. Map each value to a list of its indices, and decide how to
#      handle duplicates (e.g. return value pairs through a set).
#   Q: What if the data doesn't fit in memory?
#   A: Partition by a key shared by x and target - x (e.g. min(x, target - x)), so each
#      pair lands in one partition, then solve each partition in memory.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
