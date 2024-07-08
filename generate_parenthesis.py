class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add parenthesis if openN > n
        # Only add closing Parenthesis if closedN < openN
        # Valid String if OpenN == ClosedN == n
        stack = []
        result = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return  # Return when all combinations are added to the result
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()  # This is because we again call our function again basically
                # Recurse so then it will either appedn

        backtrack(0, 0)  # This line calls the backtrack function for the first time only
        # then it is recursively called in its if conditions
        #  string found
        return result
