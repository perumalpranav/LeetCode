class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        operations = []
        for l in range(len(arr), 1, -1):
            maxIndex = max(range(l), key=lambda i: arr[i]) 
            
            if maxIndex != l:
                #Flip max pancake to bottom, then flip all l of them
                operations.append(maxIndex+1)
                flip = arr[:maxIndex+1]
                arr = flip[::-1] + arr[maxIndex+1:]
                operations.append(l)
                flip = arr[:l]
                arr = flip[::-1] + arr[l:]


        return operations