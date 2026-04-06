class Solution:
    def isValid(self, s: str) -> bool:
        brackets = set('(){}[]')
        valid_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if c in brackets:
                if c in valid_brackets:
                    if len(stack) == 0:
                        return False
                    else:
                        if stack[-1] == valid_brackets[c]:
                            stack.pop()
                        else:
                            return False
                else:
                    stack.append(c)
        
        return len(stack) == 0