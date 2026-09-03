class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = []
        for c in s:
            if c.isalnum():
                cleaned_chars.append(c.lower())
        rev_cleaned = cleaned_chars[::-1]
        if cleaned_chars == rev_cleaned:
            return True
        else:
            return False