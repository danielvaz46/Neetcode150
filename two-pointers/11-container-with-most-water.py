# LeetCode 11. Container With Most Water (NeetCode 150)
# https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Pattern: two-pointers
# Time: O(n)  Space: O(1)
# Insight:
#   - Why it works: area = width * min(left height, right height). Start with the widest
#     container. Every move shrinks the width, so the only way to do better is a taller
#     minimum. The shorter wall limits the area, and keeping it while moving the other
#     pointer can only shrink the width without raising the minimum. So always move the
#     shorter side. This rules out every pair that uses that wall, so no pair is missed.
#   - Vs the naive approach: checking every pair is O(n^2).
#   - Skipping ahead: after moving, the inner while loops pass over bars no taller than
#     the wall just discarded. Their minimum is at most height and the width is smaller,
#     so they can't beat the area already recorded. This saves area calculations and
#     doesn't change the big-O.
#   - When the walls are equal, moving either one is safe: neither can improve alone.
#   - [PYTHONIC] left, right = 0, len(heights) - 1 sets both pointers in one line.
#   - [BUILT-IN] Alternative: the brute force in one expression (O(n^2), too slow for
#     large inputs):
#         max((j - i) * min(heights[i], heights[j]) for i, j in combinations(range(len(heights)), 2))
# Interview Q&A:
#   Q: Why move the shorter pointer?
#   A: The area is capped by the shorter wall. Moving the taller pointer shrinks the width
#      without raising that cap, so it can never improve. Moving the shorter one might.
#   Q: What are the complexities?
#   A: O(n) time and O(1) space, versus O(n^2) for checking every pair.
#   Q: How is this different from Trapping Rain Water (LeetCode 42)?
#   A: Here one rectangle between two walls counts. Trapping Rain Water sums water over every
#      position, using prefix and suffix maxima or two pointers with running maxima.
#   Q: What if the walls are equal?
#   A: Moving either is safe, since neither alone can improve the area.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            max_area = max(max_area, (right - left) * height)
            if heights[left] < heights[right]:
                left += 1
                while left < right and heights[left] <= height:
                    left += 1
            else:
                right -= 1
                while left < right and heights[right] <= height:
                    right -= 1
        return max_area
