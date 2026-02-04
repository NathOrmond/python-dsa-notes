"""
Valid Anagram Problem

Clean single-entry implementation surface.
"""


class Solution:
    def solve(self, s: str, t: str) -> bool:
        """
        Implement the Valid Anagram solution here.

        Args:
            s: str
            t: str

        Returns:
            bool
        """
        occurances = dict()
        for index, char in enumerate(s):
            if char in occurances:
                occurances[char] = occurances[char] + 1
                continue
            occurances[char] = 1

        for index, char in enumerate(t):
            if not char in occurances:
                return False
            if occurances[char] is 1:
                # delete key
                del occurances[char]
                continue
            occurances[char] = occurances[char] - 1
        
        # After processing all characters in t, check if all characters matched
        return len(occurances) == 0


def valid_anagram(s: str, t: str) -> bool:
    """Thin wrapper to the canonical Solution implementation."""
    return Solution().solve(s, t)


if __name__ == "__main__":
    pass
