/*
 * 
Code
Note
Note
Testcase
Test Result
Test Result
1568. Minimum Number of Days to Disconnect Island
Solved
Hard
Topics
Companies
Hint
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 */

 class Solution {
    public int minDays(int[][] grid) {
        if (isDisconnected(grid)) return 0;  // Grid is already disconnected
        int m = grid.length, n = grid[0].length;
        
        // Try to disconnect by changing one cell
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    if (isDisconnected(grid)) return 1;  // Grid becomes disconnected after one change
                    grid[i][j] = 1;  // Revert back
                }
            }
        }
        
        // If not possible by one change, it will take 2 days
        return 2;
    }

    // Function to check if grid is disconnected (either has 0 or more than 1 islands)
    private boolean isDisconnected(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int islands = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    islands++;
                    if (islands > 1) return true;  // More than one island means disconnected
                    dfs(grid, visited, i, j);
                }
            }
        }
        
        return islands != 1;  // Return true if 0 or more than 1 island
    }

    // DFS to mark all parts of an island as visited
    private void dfs(int[][] grid, boolean[][] visited, int i, int j) {
        int m = grid.length, n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0 || visited[i][j]) return;
        
        visited[i][j] = true;
        dfs(grid, visited, i + 1, j);
        dfs(grid, visited, i - 1, j);
        dfs(grid, visited, i, j + 1);
        dfs(grid, visited, i, j - 1);
    }
}
