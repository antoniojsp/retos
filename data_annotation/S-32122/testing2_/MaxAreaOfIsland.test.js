const MaxAreaOfIsland = require('./MaxAreaOfIsland');

describe('MaxAreaOfIsland', () => {
    let solver;

    beforeEach(() => {
        solver = new MaxAreaOfIsland();
    });

    // Test with an empty grid
    test('should return 0 for an empty grid', () => {
        const grid = [];
        expect(solver.maxAreaOfIsland(grid)).toBe(0);
    });

    // Test with a grid containing only water
    test('should return 0 for a grid with only water', () => {
        const grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ];
        expect(solver.maxAreaOfIsland(grid)).toBe(0);
    });

    // Test with a grid containing only one land cell
    test('should return 1 for a grid with only one land cell', () => {
        const grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ];
        expect(solver.maxAreaOfIsland(grid)).toBe(1);
    });

    // Test with a larger grid with multiple islands
    test('should return the largest island area', () => {
        const grid = [
            [1, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 0]
        ];
        expect(solver.maxAreaOfIsland(grid)).toBe(4);
    });

    // Test with a grid where the largest island is in the middle
    test('should return the correct area for a grid with the largest island in the middle', () => {
        const grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ];
        expect(solver.maxAreaOfIsland(grid)).toBe(5);
    });

    // Test with a grid where two islands have the same largest area
    test('should return the correct area when there are two islands with the same largest area', () => {
        const grid = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ];
        expect(solver.maxAreaOfIsland(grid)).toBe(1);
    });

    // Test with a grid with no connected land (1s) horizontally or vertically
    test('should return the correct area when no connected land cells', () => {
        const grid = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ];
        expect(solver.maxAreaOfIsland(grid)).toBe(1);
    });

    // Testing larger grid with complex islands
    test('should return the correct area for a more complex grid', () => {
        const grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0]
        ];
        expect(solver.maxAreaOfIsland(grid)).toBe(5);
    });
});