class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        if word.isupper():
            return True

        for c in word[1:]:
            if c.isupper():
                return False

        return True