# Longest Substring Without Repeating Characters

<!-- vim-markdown-toc GitLab -->

* [Question](#question)
* [Constraints:](#constraints)
* [Solution -1:](#solution-1)
    * [Explanation of solution 1](#explanation-of-solution-1)
* [Solution -2:](#solution-2)
* [References](#references)

<!-- vim-markdown-toc -->

## Question

3. Longest Substring Without Repeating Characters
   Medium 37.2K 1.7K Companies

- Given a string s, find the length of the longest
- substring without repeating characters.

```sh
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

## Constraints:

```sh
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
4.9M
Submissions
14.5M
Acceptance Rate
34.0%
```

## Solution -1:

```py
myString = "pwwkew"
# Solution -1:  (Brute Force)  O(N2)
def length_of_longest_substring(s: str) -> int:
    n = len(s)
    max_len = 0
    stringMap = {}
    for i in range(n):
        for j in range(i, n):
            subString = s[i:j+1]
            if len(subString) == len(set(subString)):
                max_len = max(max_len , len(subString))
                stringMap[subString] = max_len
    print(max_len)
    return max_len

length_of_longest_substring(myString)
```

### Explanation of solution 1

Table for string "pwwkew":

| i   | j   | substr | Is all characters unique? | max_len |
| --- | --- | ------ | ------------------------- | ------- |
| 0   | 0   | p      | Yes                       | 1       |
| 0   | 1   | pw     | Yes                       | 2       |
| 0   | 2   | pww    | No                        | 2       |
| .   | .   | .      | ...                       | ......  |
| 2   | 5   | wwkew  | No                        | 3       |
| 3   | 5   | wkew   | No                        | 3       |
| 4   | 5   | kew    | Yes                       | 3       |

## Solution -2:

## References

- [Find the longest substring without repeating characters](https://www.nileshblog.tech/longest-substring-without-repeating-characters/)
