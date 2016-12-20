'''
Consider a matrix with  rows and  columns, where each cell contains either a  or a  and any cell containing a is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally; in other words, cell  is connected to cells , , , , , , , and , provided that the location exists in the matrix for that .

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.

Task
Given an  matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.

Input Format

The first line contains an integer, , denoting the number of rows in the matrix.
The second line contains an integer, , denoting the number of columns in the matrix.
Each line  of the  subsequent lines contains  space-separated integers describing the respective values filling each row in the matrix.

Constraints

Output Format

Print the number of cells in the largest region in the given matrix.

Sample Input

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output

5
Explanation

The diagram below depicts two regions of the matrix; for each region, the component cells forming the region are marked with an X:

X X 0 0     1 1 0 0
0 X X 0     0 1 1 0
0 0 X 0     0 0 1 0
1 0 0 0     X 0 0 0
The first region has five cells and the second region has one cell. Because we want to print the number of cells in the largest region of the matrix, we print .
'''


def get_biggest_region(grid):
    # Find the first 1
    # Find the next 1
    # Set current to 0 and enter the next
    biggestRegion = 0
    for n in range(0, len(grid)):
        for m in range(0, len(grid[0])):
            if grid[n][m] == 1:
                connections = DFS(grid, n, m)
                if connections > biggestRegion:
                    biggestRegion = connections
    return biggestRegion


def DFS(grid, n, m):
    maxN = len(grid) - 1
    maxM = len(grid[0]) - 1
    sum = 0
    if grid[n][m] == 0:
        return 0
    elif grid[n][m] == 1:
        sum += 1
        grid[n][m] = 0  # Searched
        # Top Left
        if n - 1 >= 0 and m - 1 >= 0:
            sum += DFS(grid, n - 1, m - 1)
        # Top Center
        if n - 1 >= 0:
            sum += DFS(grid, n - 1, m)
        # Top Right
        if n - 1 >= 0 and m + 1 <= maxM:
            sum += DFS(grid, n - 1, m + 1)
        # Center Right
        if m + 1 <= maxM:
            sum += DFS(grid, n, m + 1)
        # Bottom Right
        if n + 1 <= maxN and m + 1 <= maxM:
            sum += DFS(grid, n + 1, m + 1)
        # Bottom Center
        if n + 1 <= maxN:
            sum += DFS(grid, n + 1, m)
        # Bottom Left
        if n + 1 <= maxN and m - 1 >= 0:
            sum += DFS(grid, n + 1, m - 1)
        # Center Left
        if m - 1 >= 0:
            sum += DFS(grid, n, m - 1)
    return sum


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
