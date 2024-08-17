/*959. Regions Cut By Slashes
Solved
Medium
Topics
Companies
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\. */


class Solution {
    public int regionsBySlashes(String[] grid) {
        int n = grid.length;
        UnionFind uf = new UnionFind(4 * n * n);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int root = 4 * (i * n + j);
                char c = grid[i].charAt(j);

                // Connect the triangles within the current cell
                if (c == '/') {
                    uf.union(root, root + 3); // 0 connects to 3
                    uf.union(root + 1, root + 2); // 1 connects to 2
                } else if (c == '\\') {
                    uf.union(root, root + 1); // 0 connects to 1
                    uf.union(root + 2, root + 3); // 2 connects to 3
                } else { // space ' '
                    uf.union(root, root + 1);
                    uf.union(root + 1, root + 2);
                    uf.union(root + 2, root + 3);
                }

                // Connect to the right cell (if exists)
                if (j + 1 < n) {
                    uf.union(root + 1, 4 * (i * n + j + 1) + 3);
                }

                // Connect to the cell below (if exists)
                if (i + 1 < n) {
                    uf.union(root + 2, 4 * ((i + 1) * n + j));
                }
            }
        }

        // Count the number of unique regions
        int regions = 0;
        for (int i = 0; i < 4 * n * n; i++) {
            if (uf.find(i) == i) {
                regions++;
            }
        }

        return regions;
    }
}

class UnionFind {
    int[] parent;
    
    public UnionFind(int size) {
        parent = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
}
