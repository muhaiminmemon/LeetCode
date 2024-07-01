class Solution:
    def isValid(self, s: str) -> bool:
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching_bracket:
                if stack:
                    top_element = stack.pop()
                else:
                    return False
                if matching_bracket[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
