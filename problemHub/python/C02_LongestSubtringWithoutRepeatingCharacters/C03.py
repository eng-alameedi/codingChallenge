# This is a demo task.
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


def solution(A):
    # Filter out the negative numbers and zeros
    A = [x for x in A if x > 0]
    N = len(A)

    # Use the list itself as a "hash" of sorts
    for i in range(N):
        # While the number is in the range [1..N] and it's not in its correct position
        while 1 <= A[i] <= N and A[i] != A[A[i] - 1]:
            # Swap it with the number at its expected position
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

    # Check for the first number out of place
    for i in range(N):
        if A[i] != i + 1:
            return i + 1

    # If all numbers from 1 to N are present, the answer is N+1
    return N + 1


# Test cases
# print(solution([1, 3, 6, 4, 1, 2]))  # 5
# print(solution([1, 2, 3]))           # 4
# print(solution([-1, -3]))            # 1

A = [1, 3, 6, 4, 1, 2]
# A = [1,2,3]
# A = [-1, -3]


def missingNumber(nums):
    nums = set(sorted(nums))
    expected_sum = len(nums) * (len(nums) + 1) // 2
    actual_sum = sum(nums)
    print(A, expected_sum, actual_sum)
    print(expected_sum - actual_sum)


# missingNumber(A)


def solution(A):
    # Step 1: Filter out non-positive numbers and create a set of positives
    positives = set(x for x in A if x > 0)

    # Step 2: Use range to find the smallest positive integer not in positives
    for i in range(1, len(A) + 2):
        print(i)
        if i not in positives:
            return i


# solution(A = A)


def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)
    # Base case.
    if 1 not in nums:
        return 1
    # Replace negative numbers, zeros,
    # and numbers larger than n by 1s.
    # After this convertion nums will contain
    # only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1
    # Use index as a hash key and number sign as a presence detector.
    # For example, if nums[1] is negative that means that number `1`
    # is present in the array.
    # If nums[2] is positive - number 2 is missing.
    for i in range(n):
        a = abs(nums[i])
        # If you meet number a in the array - change the sign of a-th element.
        # Be careful with duplicates : do it only once.
        if a == n:
            nums[0] = -abs(nums[0])
        else:
            nums[a] = -abs(nums[a])
    # Now the index of the first positive number
    # is equal to first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i
    if nums[0] > 0:
        return n
    return n + 1


print(firstMissingPositive([1, 3, 6, 4, 1, 2]))  # 5
print(firstMissingPositive([1, 2, 3]))  # 4
print(firstMissingPositive([-1, -3]))  # 1


def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)):  # delete those useless elements
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(
        len(nums)
    ):  # use the index as the hash to record the frequency of each number
        nums[nums[i] % n] += n
    for i in range(1, len(nums)):
        if nums[i] / n == 0:
            return i
    return n


print(firstMissingPositive([1, 3, 6, 4, 1, 2]))  # 5
print(firstMissingPositive([1, 2, 3]))  # 4
print(firstMissingPositive([-1, -3]))  # 1
