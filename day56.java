/*
885. Spiral Matrix III
Solved
Medium
Topics
Companies
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

 

Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
*/


class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int i = rStart, j = cStart;
        int diri = 0, dirj = 1;
        int twice = 2;
        int[][] result = new int[rows * cols][2];
        int moves = 1;
        int nextMoves = 2;
        int index = 0;
        
        while (index < rows * cols) {
            if (i >= 0 && i < rows && j >= 0 && j < cols) {
                result[index++] = new int[]{i, j};
            }
            
            // Move to the next cell
            i += diri;
            j += dirj;
            moves--;
            if (moves == 0) {
                int temp = diri;
                diri = dirj;
                dirj = -temp;
                
                twice--;
                if (twice == 0) {
                    twice = 2;
                    moves = nextMoves;
                    nextMoves++;
                } else {
                    moves = nextMoves - 1;
                }
            }
        }
        
        return result;
    }
}
