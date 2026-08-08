class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stacks = []
        for c in s:
            if c not in valids:
                stacks.append(c)
            else:
                if not stacks or valids[c] != stacks[-1]:
                    return False

                stacks.pop()

        return len(stacks) == 0
