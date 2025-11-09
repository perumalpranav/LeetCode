class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        change_color = image[sr][sc]

        if change_color == color:
            return image

        def fill(r, c):
            if image[r][c] == change_color:
                image[r][c] = color

                if r + 1 < rows:
                    fill(r+1, c)
                if c + 1 < cols:
                    fill(r, c+1)
                if r - 1 >= 0:
                    fill(r-1, c)
                if c - 1 >= 0:
                    fill(r, c-1)
        
        fill(sr,sc)
        return image
        