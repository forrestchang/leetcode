class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lines = len(grid)
        rows = len(grid[0])
        island, neighbours = 0, 0
        for i in range(lines):
            for j in range(rows):
                if grid[i][j] == 1:
                    island += 1
                    if i < lines - 1 and grid[i+1][j] == 1:
                        neighbours += 1
                    if j < rows - 1 and grid[i][j+1] == 1:
                        neighbours += 1
        return island * 4 - 2 * neighbours

if __name__ == '__main__':
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    print(Solution().islandPerimeter(grid))
    assert Solution().islandPerimeter(grid) == 16
