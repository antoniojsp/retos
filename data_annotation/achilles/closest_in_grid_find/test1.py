# .0..0
# .....
# .0...
# .....
# 0....


def find_closest_neighbors(grid):
    """Analyzes a grid of cells and identifies the closest neighbors for each node.

    Args:
      grid: A list of strings representing the grid. Each string represents a row
            in the grid, where '.' represents an empty cell and '0' represents a
            cell containing a node.

    Returns:
      A list of strings. Each string represents the coordinates of a node and its
      closest neighbors in the format 'x1 y1 x2 y2 x3 y3', where:
        (x1, y1): The coordinates of the node.
        (x2, y2): The coordinates of the closest neighbor to the right of the node.
        (x3, y3): The coordinates of the closest neighbor below the node.
      If a neighbor does not exist, the corresponding coordinates should be '-1 -1'.
    """
    height = len(grid)
    width = len(grid[0])
    output = []

    for y in range(height):
        for x in range(width):
            if grid[y][x] == '0':
                x1, y1 = x, y
                x2, y2 = -1, -1
                x3, y3 = -1, -1

                for x_neighbor in range(x + 1, width):
                    if grid[y][x_neighbor] == '0':
                        x2, y2 = x_neighbor, y
                        break

                for y_neighbor in range(y + 1, height):
                    if grid[y_neighbor][x] == '0':
                        x3, y3 = x, y_neighbor
                        break

                output.append(f"{x1} {y1} {x2} {y2} {x3} {y3}")

    return output


if __name__ == "__main__":
    width = 5
    height = 5
    grid = [
        ['.', '0', '.', '.', '0'],
        ['.', '.', '.', '.', '.'],
        ['.', '0', '.', '.', '.'],
        ['.', '0', '.', '.', '.'],
        ['0', '.', '.', '.', '0']
    ]

    neighbors = find_closest_neighbors(grid)
    for line in neighbors:
        print(line)