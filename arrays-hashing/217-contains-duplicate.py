# LeetCode 217. Contains Duplicate (NeetCode 150)
# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Pattern: arrays-hashing
# Time: O(n)  Space: O(n)
# Insight:
#   - Alternative: loop with a "seen" set and return True on the first repeat.
#     Same big-O, but it can exit early when a duplicate appears near the front.
# Interview Q&A:
#   Q: Compare the approaches.
#   A: Set: O(n) time, O(n) space. Sort and compare neighbours: O(n log n) time, O(1) extra
#      space if sorted in place. Brute force: O(n^2) time, O(1) space.
#   Q: What if memory is tight?
#   A: Sort in place and compare adjacent elements, trading time for space.
#   Q: What if duplicates only count within k positions of each other (LeetCode 219)?
#   A: Keep a sliding window set of the last k elements.
#   Q: Why is the seen-set loop sometimes faster than len(set(nums))?
#   A: It stops at the first repeat. len(set(nums)) always builds the whole set.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
