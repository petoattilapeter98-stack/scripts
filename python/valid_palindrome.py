# Task 2: Valid Palindrome
# Description
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

import unittest

class TestPalindrome(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_palindrome_comp("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome_comp("race a car"))
        self.assertTrue(is_palindrome_comp(" "))
        self.assertTrue(is_palindrome_comp("12321"))

        self.assertTrue(is_palindrome_slicing("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome_slicing("race a car"))
        self.assertTrue(is_palindrome_slicing(" "))
        self.assertTrue(is_palindrome_slicing("12321"))

def is_palindrome_slicing(text):
    # Remove special characters
    clean_text = ''.join([char for char in text if char.isalnum()])
    # Lowercase text
    clean_text = clean_text.lower()
    
    # if the text equals with the reversed text it returns True (with sliceing)
    if clean_text == clean_text[::-1]:
        return True

    return False

def is_palindrome_comp(text):
    # Remove special characters
    text = ''.join([char for char in text if char.isalnum()])
    # Lowercase text
    text = text.lower()

    # Iterates through the the first half of the string. If the text char length is odd, it ignores the char in the middle (it doesnt count)
    for i in range(0, len(text)//2):
        # Compares the characters from the beggining with the end of the characters and goes to the center like a mirror
        if text[i] != text[len(text)-i-1]:
            # If it finds two craracters in the mirror comparison which are not equal, returns False
            return False

    # If every characters were equal, it return True as it is a palindrome
    return True

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
