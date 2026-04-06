class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set('+-*/')
        stack = []
        for token in tokens:
            print(stack)
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                c = 0
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                else:
                    c = int(a / b)
                stack.append(c)

        return stack[0]