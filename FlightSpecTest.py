import unittest

from FlightSpec import isValidSpecLength
from FlightSpec import isValidSpec
from FlightSpec import isFirstThreeDigitsValid
from FlightSpec import isFourthDigitValid
from FlightSpec import isFifthDigitValid
from FlightSpec import isSixthDigitValid
from FlightSpec import isSeventhDigitValid
from FlightSpec import isNinthDigitValid
from FlightSpec import isTenthDigitValid
from FlightSpec import isEleventhDigitValid
from FlightSpec import isTwelveDigitValid



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

    def test_validSeventhAndEighthChar(self):
        result = isSeventhDigitValid('ABC 456789AB')
        self.assertTrue(result, 'The seven and eighth digit is valid')

    def test_validSeventhAndEighthZeroChar(self):
        result = isSeventhDigitValid('ABC 111009AB')
        self.assertTrue(result, 'The seven and eighth digit is valid')

    def test_validSeventhAndEighthNineChar(self):
        result = isSeventhDigitValid('ABC 111999AB')
        self.assertTrue(result, 'The seven and eighth digit is valid')

    def test_invalidSeventhAndEighthChar(self):
        result = isSeventhDigitValid('ABC 456AB89AB')
        self.assertTrue(result, 'The seven and eighth digit is valid')
    
    def test_validNinthChar(self):
        result = isTenthDigitValid('ABC 456ANN9AB')
        self.assertTrue(result, 'The ninth digit is valid')
    
    def test_validTenthChar(self):
        result = isTenthDigitValid('ABC 456ANB9AB')
        self.assertFalse(result, 'The tenth digit is invalid')

    def test_validEleventhChar(self):
        result = isEleventhDigitValid('ABC 456ANB AB')
        self.assertTrue(result, 'The eleventh digit is valid')
    
    def test_invalidEleventhChar(self):
        result = isEleventhDigitValid('ABC 456ANBAB')
        self.assertFalse(result, 'The eleventh digit is invalid')
    
    def test_validTwelvethChar(self):
        result = isTwelveDigitValid('ABC 456ANBAE')
        self.assertTrue(result, 'The twelveth digit is valid')

    def test_invalidTwelvethChar(self):
        result = isTwelveDigitValid('ABC 456ANBAS')
        self.assertFalse(result, 'The twelveth digit is invalid')

if __name__ == '__main__':
    unittest.main()