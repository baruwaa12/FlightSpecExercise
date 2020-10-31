import unittest

from FlightSpec import isValidSpecLength
from FlightSpec import isValidSpec
from FlightSpec import isFirstThreeDigitsValid
from FlightSpec import isFourthDigitValid
from FlightSpec import isFifthDigitValid
from FlightSpec import isSixthDigitValid
from FlightSpec import isSeventhDigitValid



class FlightSpecTest(unittest.TestCase):

    def test_spec_length_is_invalid(self):
        result = isValidSpecLength('ABCDE')
        self.assertFalse(result, 'Test length is invalid')
        
    def test_spec_length_is_valid(self):
        result = isValidSpecLength('0123456789AB')
        self.assertTrue(result, 'Test length is invalid')

    def test_flight_spec(self):
        result = isValidSpec('AMS 0 25 S E')
        self.assertTrue(result, 'Test Spec is incorrect')

    def test_validFirstThreeDigits(self):
        result = isFirstThreeDigitsValid('ABC3456789AB')
        self.assertTrue(result, 'First three digits are letters')

    def test_invalidFirstThreeDigits(self):
        result = isFirstThreeDigitsValid('123456789AB')
        self.assertFalse(result, 'First three digits must be letters')
    
    def test_validFourthChar(self):
        result = isFourthDigitValid('ABC 456789AB')
        self.assertTrue(result, 'The fourth digit needs to have a space')

    def test_invalidFourthChar(self):
        result = isFourthDigitValid('123456789AB')
        self.assertFalse(result, 'The fourth digit does not have a space')

    def test_validFifthChar(self):
        result = isFifthDigitValid('01232')
        self.assertTrue(result, 'The fifth digit is less than and equal to 3')

    def test_invalidFifthChar(self):
        result = isFifthDigitValid('01235')
        self.assertFalse(result, 'The fifth digit needs to be less than 3')

    def test_validSixthChar(self):
        result = isSixthDigitValid('ABC 4 56 789AB')
        self.assertTrue(result, 'The sixth digit is a space')
    
    def test_invalidSixthChar(self):
        result = isSixthDigitValid('ABC 456789AB')
        self.assertFalse(result, 'The sixth digit needs to have a space')

    def test_validSeventhandEighthChar(self):
        result = isSeventhDigitValid('ABC 456789AB')
        self.assertTrue(result, 'The seven and eighth digit is valid')



if __name__ == '__main__':
    unittest.main()