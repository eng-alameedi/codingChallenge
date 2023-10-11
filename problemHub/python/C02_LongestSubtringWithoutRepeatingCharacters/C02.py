# myString = "abcabcbcdef"
myString = ["aabhklmnop", "pwwkew"]


# Solution -1:  (Brute Force)  O(N2)
def length_of_longest_substring(s: str) -> int:
    n = len(s)
    max_len = 0
    stringMap = {}
    for i in range(n):
        for j in range(i, n):
            subString = s[i : j + 1]
            if len(subString) == len(set(subString)):
                max_len = max(max_len, len(subString))
                k
    return max_len


# length_of_longest_substring(myString)

# Solution -2: Sliding Window


def length_of_longest_substringII(s: str) -> int:
    n = len(s)
    max_len = 0
    left, right = 0, 0
    chars = set()

    while right < n:
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            max_len = max(max_len, right - left)
        else:
            chars.remove(s[right])
            left += 1
    print(f"string -> {s:10s}, max len: {max_len}")


# Solution -3: SLiding Window Optimized
def length_of_longest_substringIII(s: str) -> int:
    # n = len(s)
    max_len = 0
    left = 0
    char_index = {}  # stores character and its latest index
    for right, char in enumerate(s):
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    print(f"string -> {s:10s}, max len: {max_len}")

    return max_len


for s in myString:
    length_of_longest_substringIII(s=s)

    # while right < n:
    #     if s[right] not in chars:
    #         chars.add(s[right])
    #         max_len = max(max_len, right - left + 1)
    #         right += 1
    #         print(f"string: {s}, right: {right}, left: {left}, char: {chars}, s[left]: {s[left]}, s[right]: {s[right]},  max_len: {max_len}")
    #     else:
    #         chars.remove(s[left])
    #         left += 1
    #
