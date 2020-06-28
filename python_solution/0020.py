class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in {'(', '{', '['}:
                stack.append(item)
            else:
                # To avoid pop the empty list
                if not stack: return False
                tail = stack.pop()
                if (tail == '(' and item == ')') or (tail == '[' and item == ']') or (tail == '{' and item == '}'):
                    continue
                else:
                    return False
        # If stack is empty after one pass, then return True
        return len(stack)==0