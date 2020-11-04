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
from FlightSpec import getDestination
from FlightSpec import getFlightCost
from FlightSpec import getBaggageCosts
from FlightSpec import getSeatingClass
from FlightSpec import MealCost
from FlightSpec import discounts
from FlightSpec import totalCost

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
        self.assertFalse(result, 'First three digits are letters')

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
    
    def test_validSpec(self):
        result = isValidSpec('AMS 0 25 S E')
        self.assertTrue(result, 'This Spec is valid')
    
    def test_getDestinationSchiphol(self):
        result = getDestination('AMS 0 25 S E')
        self.assertEqual(result, 'Schiphol, Amsterdam', 'destination should be Amsterdam')
    
    def test_getDestinationGlasgow(self):
        result = getDestination('GLA 0 25 S E')
        self.assertEqual(result, 'Glasgow, Scotland', 'destination should be Scotland')
    
    def test_getDestinationUnknown(self):
        result = getDestination('ABC 0 25 S E')
        self.assertEqual(result, 'Unknown destination', 'destination should be Unknown')
    
    def test_getFlightCostAMS(self):
        result = getFlightCost('AMS 0 25 S E')
        self.assertEqual(result, 150.00, 'AMS cost should be 150')
    
    def test_getFlightCostGLA(self):
        result = getFlightCost('GLA 0 25 S E')
        self.assertEqual(result, 80.00, 'GLA cost should be 80')
    
    def test_getFlightCostUnknown(self):
        result = getFlightCost('ABC 0 25 S E')
        self.assertEqual(result, -1, 'Unknown cost should be -1')
    
    def test_getBaggageCostsGLANoBags(self):
        result = getBaggageCosts('GLA 0 25 S E')
        self.assertEqual(result, 0.00, 'GLA no bags should be 0')
    
    def test_getBaggageCostsAMSNoBags(self):
        result = getBaggageCosts('AMS 0 25 S E')
        self.assertEqual(result, 0.00, 'AMS no bags should be 0')
    
    
    def test_getBaggageCostsGLAWithBags(self):
        result = getBaggageCosts('GLA 2 25 S E')
        self.assertEqual(result, 20.00, 'GLA with 2 bags should be 20')

    def test_getBaggageCostsAMSWithBags(self):
        result = getBaggageCosts('AMS 2 25 S E')
        self.assertEqual(result, 20.00, 'AMS with 2 bags should be 20')

    def test_getBaggageCostsGLAFirstBagFree(self):
        result = getBaggageCosts('GLA 1 25 S E')
        self.assertEqual(result, 0.00, 'AMS First bag should be free')

    def test_getBaggageCostsAMSFirstBagFree(self):
        result = getBaggageCosts('AMS 1 25 S E')
        self.assertEqual(result, 0.00, 'AMS First bag should be free')
    
    def test_getSeatingClassEconomy(self):
        result = getSeatingClass('AMS 1 25 S E')
        self.assertEqual(result, 'Economy', 'The seating class should be economy')

    def test_getSeatingClassFirstClass(self):
        result = getSeatingClass('AMS 1 25 S F')
        self.assertEqual(result, 'First Class', 'The seating class should be First Class')
    
    def test_getMealCostStandard(self):
        result = MealCost('AMS 1 25 S F')
        self.assertEqual(result, 10.00, 'The Meal Cost should be 10.00')

    def test_getMealCostNoMeal(self):
        result = MealCost('AMS 1 25 N F')
        self.assertEqual(result, 0.00, 'The Meal Cost should be 0.00')
    
    def test_getMealCostVegetarian(self):
        result = MealCost('AMS 1 25 V F')
        self.assertEqual(result, 12.00, 'The Meal Cost should be 12.00')
    
    def test_DiscountsChildEconomyAMS(self):
        result = discounts('AMS 1 15 V E')
        self.assertEqual(result, 77.50, 'The Flight cost should be 77.50')

    def test_ChildDiscountEconomyGLA(self):
        result = discounts('GLA 1 15 V E')
        self.assertEqual(result, 42.50, 'The Total discount cost should be 42.50')

    def test_NoChildDiscountEconomyGLA(self):
        result = discounts('GLA 1 21 V E')
        self.assertEqual(result, 0.00, 'The total discount should be 0.00')
    
    def test_FinalCostTestAMSE(self):
        result = totalCost('AMS 0 25 S E')
        self.assertEqual(result, 160.00, 'The final cost should be 160.00')
    
    def test_FinalCostTestAMSF(self):
        result = totalCost('AMS 0 25 S F')
        self.assertEqual(result, 910.00, 'The final cost should be 910.00')

        

if __name__ == '__main__':
    unittest.main()