class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        if m == 1:
            return [1] * n
        
        rem = int(word[0]) % m
        if rem == 0:
            ans = [1]
        else:
            ans = [0]

        for i in range(1,n):
            rem = (rem * 10) + int(word[i])
            print(f"{i} {rem}")
            rem = rem % m
            if rem == 0:
                ans.append(1)
            else:
                ans.append(0)

        return ans