class Solution:
    def isFascinating(self, n: int) -> str:
        concatenated = str(n) + str(2 * n) + str(3 * n)
        return sorted(concatenated) == list('123456789')


# You are given an integer n that consists of exactly 3 digits.

# We call the number n fascinating if, after the following modification, 
# the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:
# Example 1:

# Input: n = 192
# Output: true
# Explanation: We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576. 
# The resulting number is 192384576. This number contains all the digits from 1 to 9 exactly once.