class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == '+':
                second = stack.pop()
                first = stack.pop()
                value = int(first) + int(second)
                stack.append(value)
            elif char == '-':
                second = stack.pop()
                first = stack.pop()
                value = int(first) - int(second)
                stack.append(value)
            elif char == '*':
                second = stack.pop()
                first = stack.pop()
                value = int(first) * int(second)
                stack.append(value)
            elif char == '/':
                second = stack.pop()
                first = stack.pop()
                value = int(float(first) / second)
                stack.append(value)
            else:
                stack.append(int(char))
        
        return stack[-1]