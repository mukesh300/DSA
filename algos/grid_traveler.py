# brute force
def grid_traveller(rows, cols):
    if rows < 1 or cols < 1:
        return 0
    if rows == 1 or cols == 1:
        return 1
    return grid_traveller(rows - 1, cols) + grid_traveller(rows, cols - 1)

# memoization
def grid_traveller_m(rows, cols, memo={}):
    if (rows, cols) in memo:
        return memo[(rows, cols)]
    if rows < 1 or cols < 1:
        return 0
    if rows == 1 or cols == 1:
        return 1
    memo[(rows, cols)] = grid_traveller(rows - 1, cols) + grid_traveller(rows, cols - 1)
    return memo[(rows, cols)]

# tabulation
def grid_traveller_t(rows, cols):
    grid = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        grid[0][i] = 1
    for i in range(cols):
        grid[i][0] = 1
    for row in range(1, rows):
        for col in range(1, cols):
            grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
    return grid[rows - 1][cols - 1]


if __name__ == "__main__":
    print(grid_traveller(5, 5))
    print(grid_traveller_m(5, 5))
    print(grid_traveller_t(5, 5))
