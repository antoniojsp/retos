class MaxAreaOfIsland {
    // Method to find the maximum area of an island in a 2D grid
    maxAreaOfIsland(grid) {
        let max = 0;

        // Iterate through each cell in the grid
        for (let i = 0; i < grid.length; i++) {
            for (let j = 0; j < grid[i].length; j++) {
                // If the cell contains land (1), initiate a depth-first search
                if (grid[i][j] === 1) {
                    let count = 0;
                    max = Math.max(max, this.dfs(grid, i, j, count));
                }
            }
        }

        return max;
    }

    // Depth-first search to explore the island and calculate its area
    dfs(grid, i, j, count) {
        // Base cases: out of bounds or cell is water (0)
        if (
            i < 0 ||
            j < 0 ||
            i >= grid.length ||
            j >= grid[0].length ||
            grid[i][j] === 0
        ) {
            return 0;
        }

        // Mark the current cell as visited (0) and explore its neighbors
        grid[i][j] = 0;
        return (
            1 +
            this.dfs(grid, i, j - 1, count) +
            this.dfs(grid, i, j + 1, count) +
            this.dfs(grid, i - 1, j, count) +
            this.dfs(grid, i + 1, j, count)
        );
    }
}

module.exports = MaxAreaOfIsland;