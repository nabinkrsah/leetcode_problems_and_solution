/*264. Ugly Number II
Solved
Medium
Topics
Companies
Hint
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
 */


 import java.util.PriorityQueue;
import java.util.HashSet;

class Solution {
    public int nthUglyNumber(int n) {
        // Min-Heap to store the next potential ugly numbers
        PriorityQueue<Long> minHeap = new PriorityQueue<>();
        // Set to track numbers already added to the heap
        HashSet<Long> seen = new HashSet<>();
        
        // Initial ugly number
        minHeap.add(1L);
        seen.add(1L);
        
        // Variables to store factors
        long[] factors = {2, 3, 5};
        
        // Variable to store the current ugly number
        long uglyNumber = 1;
        
        for (int i = 0; i < n; i++) {
            // Get the smallest number from the heap
            uglyNumber = minHeap.poll();
            
            // Generate new ugly numbers by multiplying the smallest number by 2, 3, and 5
            for (long factor : factors) {
                long newUgly = uglyNumber * factor;
                
                // Add new ugly number to heap and set if not already present
                if (seen.add(newUgly)) {
                    minHeap.add(newUgly);
                }
            }
        }
        
        // Return the nth ugly number
        return (int) uglyNumber;
    }
}
