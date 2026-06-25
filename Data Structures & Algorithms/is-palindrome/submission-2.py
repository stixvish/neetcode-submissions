class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum()).lower()
        # indices
        i, j = 0, len(cleaned) - 1
        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1
        return True