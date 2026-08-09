class Solution:
    def scoreBalance(self, s: str) -> bool:
        alphabet_dict = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 
            'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 
            'w': 23, 'x': 24, 'y': 25, 'z': 26
        }

        left = 0
        right = sum(alphabet_dict[c] for c in s)

        for i in range(len(s)):
            print(f"left {left} right {right}")
            if left == right:
                return True
            else:
                left += alphabet_dict[s[i]]
                right -= alphabet_dict[s[i]]
        
        return False