'''1717. Maximum Score From Removing Substrings
Solved
Medium
Topics
Companies
Hint
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20'''



class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_pairs(s, a, b, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return "".join(stack), score
        
        if x > y:
            s, score1 = remove_pairs(s, 'a', 'b', x)
            _, score2 = remove_pairs(s, 'b', 'a', y)
        else:
            s, score1 = remove_pairs(s, 'b', 'a', y)
            _, score2 = remove_pairs(s, 'a', 'b', x)
        
        return score1 + score2
