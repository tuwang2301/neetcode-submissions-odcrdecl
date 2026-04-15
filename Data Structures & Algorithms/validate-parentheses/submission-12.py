class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
        }

        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False

        return len(stack) == 0
