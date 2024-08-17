/* 
1653. Minimum Deletions to Make String Balanced
Solved
Medium
Topics
Companies
Hint
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
*/


class Solution {
    public int minimumDeletions(String s) {
        int n = s.length();
        int[] prefixBCount = new int[n + 1]; 
        int[] suffixACount = new int[n + 1]; 
        
        for (int i = 0; i < n; i++) {
            prefixBCount[i + 1] = prefixBCount[i] + (s.charAt(i) == 'b' ? 1 : 0);
        }
        for (int i = n - 1; i >= 0; i--) {
            suffixACount[i] = suffixACount[i + 1] + (s.charAt(i) == 'a' ? 1 : 0);
        }
        
        int minDeletions = Integer.MAX_VALUE;
        for (int i = 0; i <= n; i++) {
            minDeletions = Math.min(minDeletions, prefixBCount[i] + suffixACount[i]);
        }
        
        return minDeletions;
    }
}
