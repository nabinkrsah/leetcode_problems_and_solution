'''726. Number of Atoms
Solved
Hard
Topics
Companies
Hint
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 '''
 
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import collections
        
        self.i = 0
        self.formula = formula
        self.n = len(formula)

        def parse_atom():
            start = self.i
            self.i += 1  # we know formula[self.i] is a letter
            while self.i < self.n and self.formula[self.i].islower():
                self.i += 1
            return self.formula[start:self.i]

        def parse_num():
            if self.i == self.n or not self.formula[self.i].isdigit():
                return 1
            start = self.i
            while self.i < self.n and self.formula[self.i].isdigit():
                self.i += 1
            return int(self.formula[start:self.i])

        stack = [collections.Counter()]
        while self.i < self.n:
            if self.formula[self.i] == '(':
                self.i += 1
                stack.append(collections.Counter())
            elif self.formula[self.i] == ')':
                self.i += 1
                num = parse_num()
                top = stack.pop()
                for k, v in top.items():
                    stack[-1][k] += v * num
            else:
                atom = parse_atom()
                num = parse_num()
                stack[-1][atom] += num

        count = stack.pop()
        return "".join(atom + (str(count[atom]) if count[atom] > 1 else '')
                       for atom in sorted(count))
