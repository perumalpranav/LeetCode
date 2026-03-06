class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        optionsDict = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"]
        }

        output = []

        def dfs(digits, current = ""):
            if digits == "":
                output.append(current)
                return

            num = int(digits[0])

            for let in optionsDict[num]:
                dfs(digits[1:], f"{current}{let}")

        
        dfs(digits)
        
        return output
        
