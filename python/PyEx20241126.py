from typing import List

def hasDuplicate(nums: List[int]):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for v in d.values():
        if v >= 2:
            return True
    return False

def hasDuplicateBruteForce(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_map = {}
    t_map = {}

    for i in s:
        if i in s_map:
            s_map[i] += 1
        else:
            s_map[i] = 1

    for j in t:
        if j in t_map:
            t_map[j] += 1
        else:
            t_map[j] = 1            

    return s_map == t_map

def twoSumBruteForce(nums, target):
    d = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                d.append((i, j))
    return ", ".join(str(item) for item in d)

def twoSum(nums, target):
    d = {}
    for k, v in enumerate(nums, 0):
        if (target-v) in d:
            return (d[target-v], k)
        d[v] = k




nums = [1,2,3,4,5]
# print(hasDuplicate(nums))
# print(isAnagram('bbcc','ccbc'))
# print(twoSumBruteForce([3,4,5,6], 8))
print(twoSum([3,4,5,6], 8))
# 8-0
# 8-1






