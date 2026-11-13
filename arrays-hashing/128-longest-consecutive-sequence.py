# LeetCode 128. Longest Consecutive Sequence (NeetCode 150)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
# Pattern: arrays-hashing
# Time: O(n)  Space: O(n)
# Insight:
#   - Why it works: build the full set first so every membership check sees all the
#     numbers. A run starts at num only if num - 1 is not in the set, so counting
#     happens only from run starts. Each run is walked once and each number is
#     visited at most twice (outer loop, one walk), which is O(n) overall.
#   - Vanilla: walking up from every number is O(n^2) in the worst case (e.g. 1..n,
#     where every number re-walks the rest of the run). Sorting is O(n log n).
#   - [DECISION] Full set first vs build as you go: if each answer is found at its later
#     element (Two Sum, 217), build as you go and exit early. Here the run-start check
#     is an absence test ("num - 1 not in set") and the walk looks ahead at numbers that
#     may come later, so the whole set is needed first. Absence can't be confirmed
#     until everything is inserted.
#   - Membership must be on a set, not the list: "x in nums" is an O(n) scan.
#   - Iterating num_set instead of nums skips duplicates for free.
#   - [PYTHONIC] set(nums) builds the set in one call, and end - num gives the run
#     length without a separate counter.
#   - Alternative: sorted(set(nums)) and scan, extending the streak while the next
#     value is previous + 1. Simpler to reason about, but O(n log n).
# Interview Q&A:
#   Q: There is a while loop inside a for loop. Why is it O(n)?
#   A: Only run starts walk, and each number is walked at most once, so total work is at
#      most about 2n steps.
#   Q: What other approaches exist?
#   A: Sort and scan (O(n log n)). Union-find over adjacent values (about O(n)). A dict of
#      run lengths at the run endpoints, merging runs as each number is added (O(n)).
#   Q: How do duplicates affect it?
#   A: The set removes them, and iterating the set avoids repeating work.
#   Q: What if numbers arrive as a stream?
#   A: Keep run lengths at the endpoints and merge neighbouring runs on each arrival, so
#      the longest run updates in O(1) per number.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:   # num starts a run
                end = num + 1
                while end in num_set:
                    end += 1
                longest = max(longest, end - num)
        return longest
