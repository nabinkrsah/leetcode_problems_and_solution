/*
 * 1937. Maximum Number of Points with Cost
Solved
Medium
Topics
Companies
Hint
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
 

Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
Example 2:


Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.
 */


 class Solution {
    public long maxPoints(int[][] points) {
        int m = points.length;
        int n = points[0].length;
        long[] prevRow = new long[n];
        
        // Initialize the first row
        for (int j = 0; j < n; j++) {
            prevRow[j] = points[0][j];
        }
        
        // Iterate over the rows
        for (int i = 1; i < m; i++) {
            long[] leftMax = new long[n];
            long[] rightMax = new long[n];
            long[] currentRow = new long[n];
            
            // Calculate left to right max
            leftMax[0] = prevRow[0];
            for (int j = 1; j < n; j++) {
                leftMax[j] = Math.max(leftMax[j - 1] - 1, prevRow[j]);
            }
            
            // Calculate right to left max
            rightMax[n - 1] = prevRow[n - 1];
            for (int j = n - 2; j >= 0; j--) {
                rightMax[j] = Math.max(rightMax[j + 1] - 1, prevRow[j]);
            }
            
            // Calculate the current row based on the maximum from both sides
            for (int j = 0; j < n; j++) {
                currentRow[j] = points[i][j] + Math.max(leftMax[j], rightMax[j]);
            }
            
            // Update prevRow to currentRow for the next iteration
            prevRow = currentRow;
        }
        
        // The result is the maximum value in the last row
        long maxPoints = 0;
        for (long val : prevRow) {
            maxPoints = Math.max(maxPoints, val);
        }
        
        return maxPoints;
    }
}
