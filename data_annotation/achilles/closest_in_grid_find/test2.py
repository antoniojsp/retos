def find_closest_neighbors(grid):
    height = len(grid)
    width = len(grid[0])
    nodes = []
    results = []

    # Find all nodes
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '0':
                nodes.append((x, y))

    for node in nodes:
        x1, y1 = node
        x2, y2, x3, y3 = -1, -1, -1, -1

        # Find closest neighbor to the right
        for x in range(x1 + 1, width):
            if grid[y1][x] == '0':
                x2, y2 = x, y1
                break

        # Find closest neighbor below
        for y in range(y1 + 1, height):
            if grid[y][x1] == '0':
                x3, y3 = x1, y
                break

        results.append(f"{x1} {y1} {x2} {y2} {x3} {y3}")

    return results

# Read input
width = 5
height = 5
grid = [
    ['.', '0', '.', '.', '0'],
    ['.', '.', '.', '.', '.'],
    ['.', '0', '.', '0', '.'],
    ['.', '.', '.', '0', '.'],
    ['0', '.', '.', '.', '0']
]

# Process and output results
for result in find_closest_neighbors(grid):
    print(result)