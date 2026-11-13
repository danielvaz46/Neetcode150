# LeetCode 15. 3Sum (NeetCode 150)
# https://leetcode.com/problems/3sum/
# Difficulty: Medium
# Pattern: two-pointers
# Time: O(n^2)  Space: O(1) extra (ignoring the output and the sort)
# Insight:
#   - Why it works: sort, then fix nums[i] and solve Two Sum II (167) on the numbers to
#     its right for a pair summing to -nums[i]. Sorting is what makes the pointer moves
#     valid and puts equal values next to each other. The sort is O(n log n), dominated
#     by the O(n) pointer sweep run for each of the n values of i.
#   - Vs the naive approach: three nested loops are O(n^3), and need a set of tuples to
#     remove duplicate triplets.
#   - Duplicates are skipped by position, so no set is needed:
#       - skip nums[i] if it equals nums[i - 1] (same first number, same triplets);
#       - after recording a triplet, move both pointers, then keep moving each past
#         values equal to the one it just left.
#   - range(n - 2) stops once fewer than three numbers remain.
#   - nums.sort() sorts in place and changes the caller's list; sorted(nums) would copy.
#   - Early exit: break once nums[i] > 0, since everything after it is also positive and
#     can't sum to 0.
#   - [BUILT-IN] Alternative: itertools.combinations is the shortest version, but it is
#     the O(n^3) brute force, so it is only fine for small inputs:
#         return [list(c) for c in {*combinations(sorted(nums), 3)} if sum(c) == 0]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return res
