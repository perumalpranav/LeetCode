class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)

        def vowel(c):
            if c == 'a' or c =='e' or c == 'i' or c == 'o' or c == 'u':
                return True
            return False

        total = 0
        for i, c in enumerate(word):
            if vowel(c):
                total += (i + 1) * (n - i)

        return total
        


        
        