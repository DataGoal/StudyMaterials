import collections
def findMedianSortedArrays(ls1, ls2):
    ls3 = ls1 + ls2
    ls4 = sorted(ls3)
    mid = len(ls3) // 2
    if len(ls3) % 2 == 0:
        return (ls3[mid - 1] + ls3[mid]) / 2
    else:
        return ls3[mid]


def containsDuplicate(ls):
    if len(ls) == len(set(ls)):
        return False
    else:
        return True


def containsDuplicate2(ls):
    dict = {}
    for i in ls:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
    print(dict)
    for v in dict.values():
        if v > 1:
            return True
    return False


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_map, t_map = {}, {}
    for i in s:
        if i not in s_map:
            s_map[i] = 1
        else:
            s_map[i] += 1
    for j in t:
        if j not in t_map:
            t_map[j] = 1
        else:
            t_map[j] += 1

    return sorted(s_map.items()) == sorted(t_map.items())

def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    sCount = collections.Counter(s)
    print(sCount)
    tCount = collections.Counter(t)

    for c in sCount:
        if c not in tCount:
            return False
        if tCount[c] != sCount[c]:
            return False

    return True

def twoSum(nums, target):
    d = {}
    for k, v in enumerate(nums, 0):
        if (target - v) in d:
            return d[target - v], k
        else:
            d[v] = k



# print(findMedianSortedArrays([1, 3],[2]))
# print(containsDuplicate2([1, 2, 4]))
print(isAnagram2('bala', 'aabl'))
#print(twoSum([1, 2, 3, 5],8))
