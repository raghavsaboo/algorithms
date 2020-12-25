# 0/1 Knapsack (Distinct Ways)

## Type of Problem and General Solution Structure

> Given a target and a list of items, find the optimal (min or max) cost / path / sum to reach the target.
>
> ### General Solution Structure
>
> ```python
> """
> 1. Choose minimum/maximum path among all possible paths before the current state and add the value for the current state
> 2. Skip/Exclude current state, and process remaining items
> """
> def recursive_solution(items, target, cost):
>     
>     def recursion(items, target, cost, index):
>         if target <= 0 or index >= len(cost):
>             return 0
>         
>         cost1 = 0
>         if cost[index] <= target:
>             
> 
> def bottom_up_solution(items, target, cost)
>     for i in range(target):
>         for j in range(items):
>             if items[j] <= target:
>                 dp[i] = min(dp[i], dp[i - items[j]] + cost[j])
>     return dp[target]
> ```
>



# Unbounded Knapsack



# Numeric Series Based Problems



# Palindrome Based Problems



# Sequence Based Problems

## Longest Common Substring

> Given two strings `s1` and `s2` , find the length of the longest substring which is common in both.
>
> ```bash
> Dynamic Programming# Example 1
> > get_lcs_length(s1 = "abdca", s2 = "cbda")
> > 2
> # Example 2
> > get_lcs_length("passport", "ppsspt")
> > 3
> ```
>
> ### Solution
>
> ```python
> """
> Top Down
> Time Complexity = O(3^(m + n))
> Space Complexity = O(m * n)
> - m, n = len(s1), len(s2)
> - Create a m by n by count (= min(m, n)) array
> - [BASE CASE] If either index >= len(string), return count
> - Match strings one character at a time, with one pointer on each string
> - If char matches, increment pointers on both strings by 1
> 	- Recursively call LCS function
> - If char does not match
> 	- Increment pointer for s1 only and recursively call LCS function
> 	- Increment pointer for s2 only and recursively call LCS function
> - Keep track of longest string found and return
> """
> 
> def get_lcs_length(s1, s2):
>     n1, n2 = len(s1), len(s2)
>     max_length = min(n1, n2)
>     cache = [[[-1 for _ in range(max_length)] for _ in range(n2)] for _ in range(n1)]
>     return get_lcs_length_recursive(cache, s1, s2, 0, 0, 0)
> 
> def get_lcs_length_recursive(cache, s1, s2, index1, index2, count):
>     if index1 == len(s1) or index2 == len(s2):
>         return count
>     
>     if cache[index1][index2][count] == -1:
>         c1 = count
>         if s1[index1] == s2[index2]:
>             c1 = get_lcs_length_recursive(cache, s1, s2, index1 + 1, index2 + 1, 0)
>         c2 = get_lcs_length_recursive(cache, s1, s2, index1, index2 + 1, 0)
>         c3 = get_lcs_length_recursive(cache, s1, s2, index1 + 1, index2, 0)
>         cache[index1][index2][count] = max(c1, max(c2, c3))
>         
>      return cache[index1][index2][count]
>     
> """
> Bottom Up
> Time Complexity = O(m * n)
> Space Complexity = O(m * n)
> - m, n = len(s1), len(s2)
> - Initialize a m by n array:
> 	- if s1[i] matches s2[j] then LCS length cache[i][j] = cache[i-1][j-1] + 1
> 	- if s1[i] != s2[j] then LCS length cache[i][j] = 0
> Example:
>        a b d c a
> 	[0 0 0 0 0 0]
> c	[0 0 0 0 1 0]
> b	[0 0 1 0 0 0]
> d	[0 0 0 2 0 0]
> a	[0 1 0 0 0 1]
> """
> def get_lcs_length(s1, s2):
>     n1, n2 = len(s1), len(s2)
>     cache = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
>     max_length = 0
>     for i in range(1, n1 + 1):
>         for j in range(1, n2 + 1):
>             if s1[i - 1] == s2[j - 1]:
>                 cache[i][j] = 1 + cache[i - 1][j - 1]
>                 max_length = max(max_length, cache[i][j])
>         return max_length
> ```

## Longest Common Subsequence

> Given two strings `s1` and `s2` find the length of the longest subsequence which is common in both the strings.
>
> - a subsequence can be derived from another sequence by deleting some or no elements ==without== changing the order of the remaining elements
>
> ```bash
> # Example 1
> > get_lcs_length("abdca", "cbda")
> > 3
> # Example 2
> > get_lcs_length("passport", "ppsspt")
> > 5
> ```
>
> ### Solution
>
> ```python
> """
> Top Down
> - len(s1) x len(s2) matrix to cache results
> - Two pointers, one for each string, starting at index 0
> - [BASE CASE] If either index is >= len(string), return 0
> - If s1[index1] == s2[index2] then count = 1 + get_lcs_length(s1, s2, i1 + 1, i2 + 1)
> - If s1[index1] != s2[index2] then count
> """
> def find_LCS_length(s1, s2):
>   dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
>   return find_LCS_length_recursive(dp, s1, s2, 0, 0)
> 
> 
> def find_LCS_length_recursive(dp, s1, s2, i1, i2):
>   if i1 == len(s1) or i2 == len(s2):
>     return 0
> 
>   if dp[i1][i2] == -1:
>     if s1[i1] == s2[i2]:
>       dp[i1][i2] = 1 + find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1)
>     else:
>       c1 = find_LCS_length_recursive(dp, s1, s2, i1, i2 + 1)
>       c2 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2)
>       dp[i1][i2] = max(c1, c2)
> 
>   return dp[i1][i2]
> 
> """
> Bottom Up
> 	   c b d a
> 	[0 0 0 0 0]
> a	[0 0 0 0 1]
> b	[0 0 1 0 0]
> d	[0 0 1 2 2]
> c	[0 1 1 2 2]
> a	[0 1 1 2 3]
> - len(s1) x len(s2) matrix to cache results
> - Start at i, j = 1, 1
> - If s1[i] == s2[j] then cache[i][j] = 1 + cache[i-1][j-1]
> - Else cache[i][j] = max(cache[i-1][j], cache[i][j-1])
> """
> def find_LCS_length(s1, s2):
>   n1, n2 = len(s1), len(s2)
>   dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
>   maxLength = 0
>   for i in range(1, n1+1):
>     for j in range(1, n2+1):
>       if s1[i - 1] == s2[j - 1]:
>         dp[i][j] = 1 + dp[i - 1][j - 1]
>       else:
>         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
> 
>       maxLength = max(maxLength, dp[i][j])
>   return maxLength
> ```

## Longest Increasing Subsequence

> Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).
>
> ```bash
> # Example 1
> > get_lis_length([4,2,3,6,10,1,12])
> > 5
> # Example 2
> > get_lis_length([-4,10,3,7,15])
> > 4
> ```
>
> ### Solution
>
> ```python
> """
> Top Down
> Time Complexity = O(n^2)
> Space Complexity = O(n^2 + n)
> - Initialize a len(nums) + 1 x len(nums) array
> - Iterate through nums list
> - [BASE CASE] If index >= len(nums) then return 0
> - If start of nums or nums[curr_index] > nums[prev_index] then count = 1 + get_lis_length(nums, curr_index + 1, curr_index)
> - Else count = get_lis_length(nums, curr_index + 1, prev_index)
> """
> 
> def find_LIS_length(nums):
>   n = len(nums)
>   dp = [[-1 for _ in range(n+1)] for _ in range(n)]
>   return find_LIS_length_recursive(dp, nums, 0, -1)
> 
> 
> def find_LIS_length_recursive(dp, nums, currentIndex, previousIndex):
>   if currentIndex == len(nums):
>     return 0
> 
>   if dp[currentIndex][previousIndex + 1] == -1:
>     # include nums[currentIndex] if it is larger than the last included number
>     c1 = 0
>     if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
>       c1 = 1 + find_LIS_length_recursive(dp, nums, currentIndex + 1, currentIndex)
> 
>     c2 = find_LIS_length_recursive(dp, nums, currentIndex + 1, previousIndex)
>     dp[currentIndex][previousIndex + 1] = max(c1, c2)
> 
>   return dp[currentIndex][previousIndex + 1]
> 
> """
> Bottom Up
> - Create list of len(nums) and initialize with 1 (each item forms LIS of 1)
> - Iterate through the nums list with two pointers - i & j where j < i
> - If nums[j] < nums[i] and cache[j] >= cache[i] then cache[i] = cache[j] + 1
> - Else no update
> """
> def find_LIS_length(nums):
>   n = len(nums)
>   dp = [0 for _ in range(n)]
>   dp[0] = 1
> 
>   maxLength = 1
>   for i in range(1, n):
>     dp[i] = 1
>     for j in range(i):
>       if nums[i] > nums[j] and dp[i] <= dp[j]:
>         dp[i] = dp[j] + 1
>         maxLength = max(maxLength, dp[i])
> 
>   return maxLength
> ```

## Maximum Sum Increasing Subsequence

> Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.
>
> ```bash
> # Example 1
> > max_sum_increasing_subsequence([4,1,2,6,10,1,12])
> > 32
> # Example 2
> > max_sum_increasing_subsequence([-4,10,3,7,15])
> > 25
> ```
>
> ### Solution
>
> Very similar to Longest Increasing Subsequence. Instead of recursion to count, use recursion on different indices to do sums. e.g. in Bottom-Up approach simply start with a len(nums) list initialized to the value of nums at each index (max sum for smallest subsequences)

## Shortest Common Super-sequence

>Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.
>
>```bash
># Example 1
>> shortest_common_supersequence('abcf', 'bdcf')
>> 5
># Example 2
>> shortest_common_supersequence('dynamic', 'programming')
>> 15
>```

## Longest Repeating Subsequence

> Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).
>
> **Example 1:**
>
> Input: “t o m o r r o w”
> Output: 2
> Explanation: The longest repeating subsequence is “or” {tomorrow}.
>
> **Example 2:**
>
> Input: “a a b d b c e c”
> Output: 3
> Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.
>
> **Example 3:**
>
> Input: “f m f f”
> Output: 2
> Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.

# Further Reading

- Subsequence Pattern Matching
- Longest Bitonic Subsequence
- Longest Alternating Subsequence
- Edit Distance
- String Interleaving