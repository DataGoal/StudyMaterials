def avgOfList(aList):
    tmp = 0
    for i in range(len(aList)):
        tmp = tmp + aList[i]
    return tmp / len(aList)


# [1, 4, 6, 8, 9]

def maxInList(aList):
    ans = aList[0]
    for i in range(len(aList)):
        if aList[i] > ans:
            ans = aList[i]
    return ans


# [7, 2, 14, 6]

def minInList(aList):
    ans = aList[0]
    for i in range(len(aList)):
        if aList[i] < ans:
            ans = aList[i]
    return ans


# [7, 2, 14, 6]

def sortListAsc(aList):
    for i in range(len(aList)):
        for j in range(i + 1, len(aList)):
            if aList[i] >= aList[j]:
                aList[i], aList[j] = aList[j], aList[i]
    return aList


def sortListDesc(aList):
    for i in range(len(aList)):
        for j in range(i + 1, len(aList)):
            if aList[i] <= aList[j]:
                aList[i], aList[j] = aList[j], aList[i]
    return aList


def quickSortAsc(arr):
    if len(arr) <= 1:
        return arr

    # Step 1: Choose a pivot element. We'll select the middle element here.
    pivot = arr[len(arr) // 2]

    # Step 2: Partition the array into three subarrays based on the pivot.
    left = [x for x in arr if x < pivot]  # Elements less than the pivot.
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot.
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot.

    # Step 3: Recursively sort the subarrays of elements less and greater than the pivot.
    left = quickSortAsc(left)  # Sort the left subarray.
    right = quickSortAsc(right)  # Sort the right subarray.

    # Step 4: Combine the sorted subarrays and the pivot to get the final sorted array.
    return left + middle + right

def quickSortDesc(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]  # Elements less than the pivot.
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot.
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot.

    left = quickSortDesc(left)  # Sort the left subarray.
    right = quickSortDesc(right)  # Sort the right subarray.

    return right + middle + left


def findChar(aStr, toFind):
    lst = []

    for i in range(len(aStr)-(len(toFind)-1)):
        lst.append(aStr[i:i+len(toFind)])
    print(lst)
    if toFind in lst:
        return True
    else:
        return False

# https://leetcode.com/problems/sort-colors/


# https://leetcode.com/problems/maximum-subarray/

if __name__ == '__main__':
    print(avgOfList([1, 4, 6, 8, 9]))
    print(maxInList([7, 2, 14, 6]))
    print(minInList([2, 7, 14, 6]))
    print(sortListAsc([1, 4, 3, 2]))
    print(sortListDesc([34, 33, 42, 5, 21]))
    print(quickSortAsc([34, 33, 42, 5, 21]))
    print(quickSortDesc([34, 33, 42, 5, 21]))
    print(findChar('sunmoonno','nn'))





