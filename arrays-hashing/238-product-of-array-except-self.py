# LeetCode 238. Product of Array Except Self (NeetCode 150)
# https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Pattern: arrays-hashing
# Time: O(n)  Space: O(1) extra (the output array doesn't count)
# Insight:
#   - Why it works: result[i] = (product of everything left of i) * (product of
#     everything right of i). Pass 1 stores the running prefix product in result,
#     pass 2 walks right to left and multiplies in the running suffix product.
#     No division needed.
#   - Vanilla: multiply all the other elements for each i is O(n^2), and total product
#     divided by nums[i] breaks on zeros (and the problem forbids division).
#   - Starting prefix and suffix at 1 means zeros, the first element and the last
#     element need no special cases: a zero just carries into every product that
#     includes it.
#   - [PYTHONIC] reversed(range(n)) reads clearer than range(n - 1, -1, -1).
# Interview Q&A:
#   Q: Why not divide the total product by nums[i]?
#   A: Zeros break it: a division by zero, and the position of a single zero needs the
#      product of all the others. The problem also forbids division.
#   Q: What is the space complexity?
#   A: O(1) extra besides the output. The prefix products are stored in result and the
#      suffix is a running variable.
#   Q: How are zeros handled?
#   A: A zero carries into every product that includes it. Two zeros give all zeros, and
#      one zero leaves only its own index non-zero, with no special case in the code.
#   Q: What about integer overflow?
#   A: Python ints are unbounded. In Java or C++ the problem guarantees results fit in 32 bits.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(n)):
            result[i] *= suffix
            suffix *= nums[i]

        return result
