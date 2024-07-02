class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0  # Initialize a counter for consecutive odd numbers

        for num in arr:  # Iterate through each number in the array
            if num % 2 != 0:  # Check if the number is odd
                count += 1  # Increment the counter if it is odd
                if count == 3:  # Check if we have found three consecutive odds
                    return True  # Return True if we found three consecutive odds
            else:
                count = 0  # Reset the counter if the number is not odd

        return False  # Return False if no three consecutive odds were found