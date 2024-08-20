/*
  1140. Stone Game II
Solved
Medium
Topics
Companies
Hint
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104


  */



public class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        // dp[i][M] represents the maximum stones Alice can get starting from pile i with M allowed moves.
        int[][] dp = new int[n][n + 1];
        int[] suffixSum = new int[n];
        
        // Calculate the suffix sum array where suffixSum[i] is the total stones from pile i to the end.
        suffixSum[n - 1] = piles[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixSum[i] = piles[i] + suffixSum[i + 1];
        }
        
        // Fill dp array
        for (int i = n - 1; i >= 0; i--) {
            for (int M = 1; M <= n; M++) {
                // If we can take all remaining piles, take them all
                if (i + 2 * M >= n) {
                    dp[i][M] = suffixSum[i];
                } else {
                    // Otherwise, try to minimize Bob's score
                    for (int X = 1; X <= 2 * M; X++) {
                        dp[i][M] = Math.max(dp[i][M], suffixSum[i] - dp[i + X][Math.max(M, X)]);
                    }
                }
            }
        }
        
        return dp[0][1];
    }
}
