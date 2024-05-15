class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        elif x == 0:
            return True
        

        original = x
        reversed_number = 0
        
        # Loop until x becomes 0
        while x > 0:
            # Extract the last digit of x
            last_digit = x % 10
            
            # Update x to remove the last digit
            x //= 10
            
            # Multiply the reversed_number by 10 and add the last digit to it
            reversed_number = reversed_number * 10 + last_digit
        
        # Compare the original number with its reversed form
        return original == reversed_number