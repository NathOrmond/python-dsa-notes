# Valid Parentheses

## Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([])"
Output: true
```

**Example 5:**
```
Input: s = "([)]"
Output: false
```

## Constraints

- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

## Approach

**Key Insight:** Use a stack to keep track of opening brackets and match them with closing brackets.

**Algorithm:**
1. Initialize an empty stack
2. Iterate through each character in the string
3. If it's an opening bracket ('(', '[', '{'), push it onto the stack
4. If it's a closing bracket (')', ']', '}'), check if the stack is empty or if the top of the stack matches the current closing bracket
5. If they match, pop from the stack; otherwise, return false
6. After processing all characters, return true if the stack is empty, false otherwise

## Time Complexity

**O(n)** - where n is the length of the string. We iterate through each character exactly once.

## Space Complexity

**O(n)** - in the worst case, we might store all opening brackets in the stack (e.g., "(((((").

## Related Problems

- Generate Parentheses
- Remove Invalid Parentheses
- Longest Valid Parentheses
