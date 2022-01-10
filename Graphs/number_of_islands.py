#Problem - https://leetcode.com/problems/number-of-islands/

def numIslands(grid) -> int:
        rows, columns = len(grid), len(grid[0])
        print(rows, columns)
        visited = [[False]*columns for row in range(rows)]
        result = 0
        for i in range(rows):
            for j in range(columns):
                if not visited[i][j] and grid[i][j] == "1":
                    q = [(i,j)]
                    visited[i][j] = True
                    while q:
                        (row, column) = q.pop(0)
                        if row<rows and column+1<columns:
                            if (not visited[row][column+1]) and grid[row][column+1] == "1":
                                q.append((row, column+1))
                                visited[row][column+1] = True
                        if row+1<rows and column<columns:
                            if (not visited[row+1][column]) and grid[row+1][column] == "1":
                                q.append((row+1, column))
                                visited[row+1][column] = True
                        if row-1>=0:
                            if (not visited[row-1][column]) and grid[row-1][column] == "1":
                                q.append((row-1, column))
                                visited[row-1][column] = True
                        if column-1>=0:
                            if (not visited[row][column-1]) and grid[row][column-1] == "1":
                                q.append((row, column-1))
                                visited[row][column-1] = True
                    result += 1
        return result

grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(numIslands(grid))