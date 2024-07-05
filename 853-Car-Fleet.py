class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Create a list of pairs (position, speed)
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        stack = []
        # Sort the pairs by position in descending order
        for p, s in sorted(pair)[::-1]:
            # Calculate the time to reach the target and append to stack
            stack.append((target - p) / s)
            # If the last fleet catches up to the previous one, merge them
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)