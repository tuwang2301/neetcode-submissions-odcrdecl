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
                print(c, brackets[c])
                stack.append(brackets[c])
                print(stack)
            else:
                if len(stack) == 0:
                    return False
                if c != stack.pop():
                    return False

        return len(stack) == 0
