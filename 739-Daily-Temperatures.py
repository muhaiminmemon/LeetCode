class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        # Initialize the answer list with zeros, same length as temperatures
        answer = [0] * len(temperatures)
        
        # Loop through each temperature with its index
        for i in range(len(temperatures)):
            # While the stack is not empty and the current temperature is greater than
            # the temperature at the index stored on the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop the index from the stack
                j = stack.pop()
                # Calculate the number of days until a warmer temperature
                answer[j] = i - j
            # Push the current index onto the stack
            stack.append(i)
        
        return answer