# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    myName = 'Bala Chandar'


def twoSum(num, target):
    # https://leetcode.com/problems/two-sum/
    d = {}
    for k, v in enumerate(num, 0):
        if (target - v) in d:
            return d[target - v], k
        else:
            d[v] = k
# print(twoSum([2, 5, 3, 6], 8))

def twoSumBruteForce(nums, target):
    comb = []
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            if (nums[i] + nums[k]) == target:
                comb.append((i, k))
    return comb

def findTheDiff(s, t):
    # https://leetcode.com/problems/find-the-difference/
    ans = 0
    for i in s:
        ans ^= ord(i)
    for i in t:
        ans ^= ord(i)
    return chr(ans)
# print(findTheDiff('abc', 'abcd'))


def containsDuplicate(nums):
    # https://leetcode.com/problems/contains-duplicate/
    d = {}
    res = ''
    counter = 0
    for i in nums:
        if i not in d:
            d[i] = 1
            res = 'No Duplicate'
            # counter = counter + 1
        else:
            # d[i] = d[i] + 1
            res = 'Duplicate Found'
            # print ('Duplicate number is: ' + str(i))
            # print ('Duplicate number index is: ' + str(counter))
    return res
# print(containsDuplicate([2, 1, 7, 4, 7]))


def rotate(nums: List[int], k: int) -> None:
    # https://leetcode.com/problems/rotate-array/
    """
    Do not return anything, modify nums in-place instead.
    """

    res = (nums[k:] + nums[:(k-len(nums))])
    return res
# print(rotate([-1, -100, 3, 99], 2))


def isAnagram(s, t):
    # https://leetcode.com/problems/valid-anagram/
    if len(s) != len(t):
        return True

    s_map, t_map = {}, {}
    for i in s:
        if i not in s_map:
            s_map[i] = 1
        else:
            s_map[i] = s_map[i] + 1

    for i in t:
        if i not in t_map:
            t_map[i] = 1
        else:
            t_map[i] = t_map[i] + 1

    sort_s_map = sorted(s_map.items(), key=lambda x: x[0])
    sort_t_map = sorted(t_map.items(), key=lambda x: x[0])

    if sort_s_map == sort_t_map:
        return True
    else:
        return False
# print(isAnagram('aacc', 'ccac'))


'''
Change values into key inside dict
dict((v,k) for k,v in d_map.items())
'''


def isPalindrome(s):
    # https://leetcode.com/problems/valid-palindrome/
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l = l + 1
            continue
        if not s[r].isalnum():
            r = r - 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l = l + 1;
        r = r - 1;
    return True


def isPal(s):
    final_str = ''.join(e for e in s if e.isalnum()).lower()
    if final_str == final_str[::-1]:
        return True
    else:
        return False
# print (isPal('A man, a plan, a canal: Panama'))


def reverseString(s: List[str]) -> None:
    # https://leetcode.com/problems/reverse-string/
    """
    Do not return anything, modify s in-place instead.
    """
    first = 0
    last = len(s) - 1

    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1
    return s
# print(reverseString(["h", "e", "l", "l", "o"]))


def moveZeroes(nums: List[int]) -> None:
    # https://leetcode.com/problems/move-zeroes/
    # count the zeros in nums
    z = nums.count(0)
    # Filter out the zeros and concat a list size z of zeros
    nums[:] = list(filter(lambda x: x != 0, nums)) + [0] * z
    return nums
# print(moveZeroes([0, 1, 0, 3, 12]))


def singleNumber(nums: List[int]) -> int:
    # https://leetcode.com/problems/single-number/
    d = {}
    res = []
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for k, v in d.items():
        if v == 1:
            res.append(k)
    return " ".join(str(x) for x in res)
# print(singleNumber([4, 1, 2, 1, 2]))


def searchTarNumIdx(nums: List[int], target: int) -> int:
    # https://leetcode.com/problems/binary-search/
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if target > mid:
            l = mid + 1
        else:
            r = mid - 1
    return 'Not Found'
# print(searchTarNumIdx([-1, 0, 3, 5, 9, 12], 9))


def maxProfitBruteForce(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit
# print(maxProfitBruteForce([7, 1, 5, 3, 6, 4]))


def maxProfit(prices):
    profit, min_buy = 0, float('inf')
    for price in prices:
        min_buy = min(min_buy, price)  # is price less than min_buy
        profit = max(profit, price - min_buy)
    return profit
# print(maxProfit([7, 1, 5, 3, 6, 4]))


def minSwapsRequired(s):
    count = 0
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            count = count + 1
    if count % 2 == 1 and n % 2 == 0:
        return -1
    return (count + 1) // 2


def lengthOfLongestSubstring(s: str) -> int:
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
    left = 0
    seen = {}
    output = 0

    for right, curr in enumerate(s):
        if curr in seen:
            left = max(left, seen[curr] + 1)
        output = max(output, right - left + 1)
        seen[curr] = right

    return output
# print(lengthOfLongestSubstring("abcabcbb"))


def oddOrEven(num):
    if num % 2 == 0:
        return "It's Even"
    else:
        return "It's Odd"
# print(oddOrEven(4))


def is_prime(n):
    if n > 2:
        for i in range(2, int(n / 2)):
            if (n % i) == 0:
                return 'It is not a prime number'
        else:
            return 'It is a prime number'
    else:
        return 'It is not a prime number'
# print(is_prime(2))


def validIP(ip: str):
    l = ip.split('.')
    try:
        if len(l) != 4:
            return 'invalid IP'

        for i in range(len(l)):
            if int(l[i]) < 0 or int(l[i]) > 256:
                return 'invalid IP'
        return 'valid IP'
    except ValueError:
        return 'invalid IP'
# print(validIP('124.0.256.213'))


def avgLenWord(inputStr: str):
    str_length = len(inputStr.split())
    l = 0
    for i in inputStr.split():
        l += len(i)
    return l / str_length
# print (avgLenWord('Find average length of word in a sentence'))


def misMatchedWords(s1: str, s2: str):
    str_3 = s1 + ' ' + s2
    d = {}
    dls = []
    for i in str_3.split():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for k, v in d.items():
        if v == 1:
            dls.append(k)
            res = ' '.join(str(x) for x in dls)
    return res
# print (misMatchedWords("Firstly this is the first string", "Next is the second string"))


def fill_most_recent_non_none_value(input):
    recent_non_none_value = None
    for i in range(len(input)):
        if input[i]:
            recent_non_none_value = input[i]
        else:
            input[i] = recent_non_none_value
    return input
# print(fill_most_recent_non_none_value([34, None, 1, 2, 3, 22, None, 23, 24, 25, None, 25, 17, 29, None, None, 1]))


def countCharInWord(word: str, chr: str):
    counter = 0
    for i in word:
        if i == chr:
            counter += 1
    return counter
# print (countCharInWord('Mississippi', 's'))


def findSeqStart(nums):
    counter = 0
    for i in sorted(nums):
        if i == counter:
            counter += 1
            continue
    return counter
# print (findSeqStart([0, 1, 4, 2]))


def charExist(s1: str, s2: str):
    if set(s1) == set(s2):
        return True
    else:
        return False
# print (charExist('caatr','tactar'))


def frndFollower(friends):
    d = {}
    for i in friends:
        if i[0] not in d:
            if len(i) > 1:
                d[i[0]] = 1
            else:
                d[i[0]] = 0
        else:
            d[i[0]] += 1
    return d
# print (frndFollower([['D'],['A','B'],['A','C'],['C','A']]))


def urlParse(url: str):
    ls = [url.split(':')[0], url.split('/')[2], url.split('?')[1]]
    return ls
# print(urlParse('https://www.example.com/some_path?some_key=some_value'))


def validParenthesis(brac: str):
    # https://leetcode.com/problems/valid-parentheses/
    if len(brac) % 2 != 0:
        return False
    d = {'}': '{', ']': '[', ')': '('}
    res = []
    d_values = d.values()
    for i in brac:
        if i in d_values:
            res.append(i)
        else:
            if len(res) > 0 and res[-1] == d[i]:
                res.pop()
            else:
                return False
    return len(res) == 0
# print (validParenthesis('()[]{}'))


def dateConvert(date: str):
    # https://leetcode.com/problems/reformat-date/
    mBank = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
        "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    year = date.split(" ")[2]
    month = mBank[date.split(" ")[1]]
    day = date.split(" ")[0][:-2]
    if int(day) < 10:
        day = '0' + str(day)
    return f'{year}-{month}-{day}'
# print (dateConvert("16th Oct 2052"))


def numDifferentIntegers(word: str):
    s = ''.join(c if c.isdigit() else ' ' for c in word)
    return len(set(d.lstrip('0') for d in s.split()))
# print (numDifferentIntegers('a123bc34d8ef34'))


def longestCommonPrefix(strs: List[str]):
    # https://leetcode.com/problems/longest-common-prefix/
    pre = strs[0]

    for i in strs:
        while not i.startswith(pre):
            # print ('aaa: ' + pre)
            pre = pre[:-1]
            # print('bbb: ' + pre)
    return pre
# print (longestCommonPrefix(['flower', 'flow', 'floyd']))


def maxSubArray(nums: List[int]) -> int:
    maxSub = nums[0]
    currSum = 0
    for i in nums:
        if currSum < 0:
            currSum = 0
        currSum = currSum + i
        maxSub = max(maxSub, currSum)
    return maxSub
# print (maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

def romanToInt(s):
    # https://leetcode.com/problems/roman-to-integer/
    result_number = 0
    prevous_number = 0
    mapping = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
    for symbol in s[::-1]:
        if mapping[symbol] >= prevous_number:
            result_number += mapping[symbol]
            print ('p ' + str(prevous_number))
            print ('r ' + str(result_number))
        else:
            result_number -= mapping[symbol]
            print('r2 ' + str(result_number))
        prevous_number = mapping[symbol]
        print('p2 ' + str(prevous_number))
    return result_number

def fizzBuzz(n):
    # https://leetcode.com/problems/fizz-buzz/
    res = []
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            res.append('FizzBuzz')
        elif i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res


def reverseNum(num):
    a = ''
    for i in num:
        a = i + a
    return a


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# print(twoSum([2, 5, 3, 6], 8))

# print(twoSumBruteForce([2, 5, 3, 6], 7))

# print (romanToInt('II'))

# print(findTheDiff('abc', 'abcd'))
#
# print(containsDuplicate([2, 1, 7, 4, 7]))
#
# print(isAnagram('aacc', 'ccac'))
#
# print (isPal('A man, a plan, a canal: Panama'))
#
# print(searchTarNumIdx([-1, 0, 3, 5, 9, 12], 9))
#
# print(maxProfitBruteForce([7, 1, 5, 3, 6, 4]))
#
# print(lengthOfLongestSubstring("abcabcbb"))
#
# print(rotate([-1, -100, 3, 99], 2))
#
# print(reverseString(["h", "e", "l", "l", "o"]))
#
# print(moveZeroes([0, 1, 0, 3, 12]))
#
# print(singleNumber([4, 1, 2, 1, 2]))
#
# print(oddOrEven(4))
#
# print(is_prime(2))
#
# print (12 % 1)
#
# print(validIP('124.0.256.213'))
#
# print (avgLenWord('Find average length of word in a sentence'))
#
# print (misMatchedWords("Firstly this is the first string", "Next is the second string"))
#
# print(fill_most_recent_non_none_value([34, None, 1, 2, 3, 22, None, 23, 24, 25, None, 25, 17, 29, None, None, 1]))
#
# print (countCharInWord('Mississippi', 's'))
#
# print (findSeqStart([0, 1, 4, 2]))
#

# print (charExist('taaack','tack'))
#
# print (frndFollower([['D'],['A','B'],['A','C'],['C','A']]))
#
# print(urlParse('https://www.example.com/some_path?some_key=some_value'))
#
# print (validParenthesis('()[]{}'))
#
# print (dateConvert("16th Oct 2052"))
#
print (numDifferentIntegers('a123bc34d8ef34'))
#
# print (longestCommonPrefix(['flower', 'flow', 'floyd']))
#
# print (maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# print (fizzBuzz(15))

print(reverseNum('123'))



