
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        tokens = [x if x in "+-/*" else int(x) for x in tokens]
        for t in tokens:
            if t in ['+', '-', '/', '*']:
                e1 = s.pop()
                e2 = s.pop()
                r = 0
                if t == '+':
                    r = e2 + e1
                elif t == '-':
                    r = e2 - e1
                elif t == '*':
                    r = e2 * e1
                else:
                    r = int(float(e2)/float(e1))
                s.append(r)
            else:
                s.append(t)

        # print s
        return s[0]
