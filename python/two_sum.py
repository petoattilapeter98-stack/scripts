# Task 1: Two Sum
# Description
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution.
# You may not use the same element twice.
# You can return the answer in any order.

# Example
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def two_sum_fixed(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def two_sum_optimized(nums, target):
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
            
if __name__ == "__main__":
    # Tests for base
    print(f"Test 1:  {two_sum_fixed([2, 7, 11, 15], 9)} | Expected: [0, 1]")
    print(f"Test 2:  {two_sum_fixed([3, 2, 4], 6)} | Expected: [1, 2]")
    print(f"Test 3:  {two_sum_fixed([3, 3], 6)} | Expected: [0, 1]")
    print(f"Test 4:  {two_sum_fixed([-1, -2, -3, -4, -5], -8)} | Expected: [2, 4]")
    print(f"Test 5:  {two_sum_fixed([1, 5, 8, 3], 11)} | Expected: [2, 3]")

    # Tests for optimized
    print(f"Test 1:  {two_sum_optimized([2, 7, 11, 15], 9)} | Expected: [0, 1]")
    print(f"Test 2:  {two_sum_optimized([3, 2, 4], 6)} | Expected: [1, 2]")
    print(f"Test 3:  {two_sum_optimized([3, 3], 6)} | Expected: [0, 1]")
    print(f"Test 4:  {two_sum_optimized([-1, -2, -3, -4, -5], -8)} | Expected: [2, 4]")
    print(f"Test 5:  {two_sum_optimized([1, 5, 8, 3], 11)} | Expected: [2, 3]")