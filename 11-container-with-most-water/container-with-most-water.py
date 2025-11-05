class Solution:
    def maxArea(self, height: List[int]) -> int:
        # A solution will always be better with a bigger wall farther to the right
        # Two pointer, one for each side of the container

        def area(i, j):
            ar = min(height[i],height[j]) * (j - i)
            return ar

        i = 0
        j = len(height) - 1
        a = area(i,j)


        while i < j:
            temp = area(i,j)
            if temp > a:
                a = temp

            if height[i] < height[j]:
                i += 1
            else:
                 j -= 1
        

        return a
            




        