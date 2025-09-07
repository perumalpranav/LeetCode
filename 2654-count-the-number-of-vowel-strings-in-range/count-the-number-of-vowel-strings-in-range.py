class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for w in words[left:right+1]:
            if w[0] == 'a' or w[0] == 'e' or w[0] == 'i' or w[0] == 'o' or w[0] == 'u':
                if w[-1] == 'a' or w[-1] == 'e' or w[-1] == 'i' or w[-1] == 'o' or w[-1] == 'u':
                    count += 1
        return count
