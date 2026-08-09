class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = set()

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    rotten.add((i,j))
                elif cell == 1:
                    fresh.add((i,j))


        time = 0
        while len(fresh) > 0:
            rotted = 0
            queue = set()
            for i, j in rotten:
                if (i-1, j) in fresh:
                    rotted += 1
                    fresh.remove((i-1, j))
                    queue.add((i-1, j))
                if (i+1, j) in fresh:
                    rotted += 1
                    fresh.remove((i+1, j))
                    queue.add((i+1, j))
                if (i, j+1) in fresh:
                    rotted += 1
                    fresh.remove((i, j+1))
                    queue.add((i, j+1))
                if (i, j-1) in fresh:
                    rotted += 1
                    fresh.remove((i, j-1))
                    queue.add((i, j-1))

            rotten = queue

            if rotted == 0 and len(fresh) > 0:
                print(fresh)
                print(rotten)
                return -1

            time += 1

        return time
