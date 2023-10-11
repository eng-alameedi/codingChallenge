# Double for loop (Brute Force)  O(N2)
def twoSum(nums: list, target: int) -> None:
    n = len(nums)
    for idx in range(n - 1):
        for jdx in range(idx + 1, n):
            if nums[idx] + nums[jdx] == target:
                print(f"found at -> {nums[idx]} + {nums[jdx]}")

# Solution 2: Two Pass Hash Table
def twoSum2(nums: list, target: int):
    numMap = {}
    n = len(nums)
    # Build the hash table
    for i in range(n):
        numMap[nums[i]] = i
    print(numMap)

    # Find the omplement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            print([i, numMap[complement]])

# Solution 3: (One-pass Hash Table)
def twoSum3(nums: list, target: int):
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            # print([i, numMap[complement]])
            print(f"Array: {nums}\t, target {target}, index: {i}, with ->  {numMap[complement]} + {i} ")
        else:
            numMap[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    #twoSum(nums, target)
    #twoSum2(nums, target)
    twoSum3(nums, target)
    nums = [3, 2, 4]
    target = 6
    #twoSum(nums, target)
    #twoSum2(nums, target)
    twoSum3(nums, target)
