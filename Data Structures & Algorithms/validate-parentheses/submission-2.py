class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = { 
            '}': '{', 
            ')': '(', 
            ']': '['
        }

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if (stack and stack[-1] != mapping[char]) or not stack:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0