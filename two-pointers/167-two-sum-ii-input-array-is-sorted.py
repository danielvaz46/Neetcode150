# LeetCode 167. Two Sum II - Input Array Is Sorted (NeetCode 150)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
# Pattern: two-pointers
# Time: O(n)  Space: O(1)
# Insight:
#   - Why it works: the array is sorted, so the sum at (left, right) tells you which
#     pointer to move. Too big: only a smaller right can help, so right -= 1. Too small:
#     only a larger left can help, so left += 1. Every move rules out one number for
#     good. If numbers[left] + numbers[right] > target, numbers[right] would overshoot
#     with any partner at or after left, so it can't be in the answer (and likewise for
#     left when the sum is too small).
#   - Vs Two Sum (1): the dict approach is also O(n) time but needs O(n) space. The sorted
#     input lets two pointers do it in O(1) space. Brute force over all pairs is O(n^2).
#   - The answer is 1-indexed, hence the +1 on both indices.
#   - The final return [0, 1] is never reached: exactly one solution is guaranteed. It
#     only satisfies the return type.
#   - [BUILT-IN] Alternative: for each i, binary search for target - numbers[i] to its
#     right with bisect, O(n log n):
#         j = bisect_left(numbers, target - numbers[i], i + 1)
#     then check j < len(numbers) and numbers[j] == target - numbers[i].
# Interview Q&A:
#   Q: Prove that moving a pointer never skips the answer.
#   A: If the sum is too big, numbers[right] plus any partner at or after left is at least as
#      big, so numbers[right] can't be in the answer. The too-small case is symmetric for left.
#   Q: Why not use the hash map from Two Sum?
#   A: It works in O(n) time but costs O(n) space. Sorted input allows O(1).
#   Q: How would you return every pair?
#   A: After a match, move both pointers and skip equal values, as in 3Sum.
#   Q: Is binary search viable?
#   A: Yes, binary search for target - numbers[i] for each i, but it is O(n log n).

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left+1, right+1]
        return [0, 1]
