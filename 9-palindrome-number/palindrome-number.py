class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False


        original = x
        reversed_num = 0

# Reverse the number
        while x > 0:
            digit = x % 10  # Get the last digit
            reversed_num = reversed_num * 10 + digit  # Append the digit to the reversed number
            x //= 10  # Remove the last digit from x

# Check if the original number is equal to the reversed number
        return original == reversed_num