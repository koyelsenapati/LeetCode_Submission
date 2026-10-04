class Solution(object):

    def isValid(self, s):

        stack = []

        for bracket in s:

            if bracket in "({[":
                stack.append(bracket)

            else:
                if not stack:
                    return False

                if ((stack[-1] == "(" and bracket == ")") or
                    (stack[-1] == "{" and bracket == "}") or
                    (stack[-1] == "[" and bracket == "]")):

                    stack.pop()

                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False