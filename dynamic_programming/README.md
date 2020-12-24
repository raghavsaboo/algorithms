# Dynamic Programming

## Longest Common Substring

> Given two strings `s1` and `s2` , find the length of the longest substring which is common in both.
>
> ```makefile
> # Example 1
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
> **Example 1:**
>
> ```
> Input: {4,2,3,6,10,1,12}
> Output: 5
> Explanation: The LIS is {2,3,6,10,12}.
> ```
>
> **Example 1:**
>
> ```
> Input: {-4,10,3,7,15}
> Output: 4
> Explanation: The LIS is {-4,3,7,15}.
> ```

$$O(n)$$ or $O(n^2)$ 

${\displaystyle \mathbf {v} ={\begin{bmatrix}v_{1}\\v_{2}\\\vdots \\v_{n}\end{bmatrix}},\ \mathbf {w} ={\begin{bmatrix}w_{1}\\w_{2}\\\vdots \\w_{m}\end{bmatrix}}.}$

