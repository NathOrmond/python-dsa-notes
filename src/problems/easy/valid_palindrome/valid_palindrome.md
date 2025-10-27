# Valid Palindrome

## Problem Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

### Example 1:
**Input:** `s = "A man, a plan, a canal: Panama"`  
**Output:** `true`  
**Explanation:** "amanaplanacanalpanama" is a palindrome.

### Example 2:
**Input:** `s = "race a car"`  
**Output:** `false`  
**Explanation:** "raceacar" is not a palindrome.

### Example 3:
**Input:** `s = " "`  
**Output:** `true`  
**Explanation:** `s` is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Approach

### Clean and Compare
1. Convert the string to lowercase
2. Filter out all non-alphanumeric characters
3. Compare each character from the start with the corresponding character from the end
4. Return `false` if any characters don't match, `true` otherwise

## Time Complexity

O(n) where n is the length of the string
- We iterate through the string twice: once to clean, once to compare

## Space Complexity

O(n) where n is the length of the string
- We create a new cleaned string

## Related Problems

- [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
- [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
