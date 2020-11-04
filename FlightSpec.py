# This function validates the flight specification length
def isValidSpecLength(flightSpec):
    if len(flightSpec) == 12:
        return True
    else:
        return False

# Validate first three digits to be either AMS or GLA
def isFirstThreeDigitsValid(flightSpec):
    firstThree = flightSpec[0:3]
    if firstThree == "AMS" or firstThree == "GLA":
        return True
    return False

# Validate fourth digit to be a space
def isFourthDigitValid(flightSpec):
    fourth = flightSpec[3]
    if fourth == ' ':
        return True

    return False

# Validation function to check number of bags
def isFifthDigitValid(flightSpec):
    fifth = flightSpec[4]
    if fifth.isdigit() == False:
        return False
    else:
        if int(fifth) <= 3 and int(fifth) >= 0:
            return True

# Validate sixth digit to be a space
def isSixthDigitValid(flightSpec):
    sixth = flightSpec[5]
    if sixth == ' ':
        return True

    return False

# Validate the age to be between 0 and 99
def isSeventhDigitValid(flightSpec):
    seventh = flightSpec[6:7]
    if seventh.isdigit() == False:
        return False

    if int(seventh) <= 99 and int(seventh) >= 0:
        return True

# Validate ninth digit to be a space
def isNinthDigitValid(flightSpec):
    ninth = flightSpec[8]
    if ninth == ' ':
        return True

    return False


# Validate the specification to have 1 of 3 meal choices
def isTenthDigitValid(flightSpec):
    tenth = flightSpec[9]
    if tenth == 'N' or tenth == 'S' or tenth == 'V':
        return True
    return False

# Validate eleventh digit to be a space
def isEleventhDigitValid(flightSpec):
    eleventh = flightSpec[10]
    if eleventh == ' ':
        return True

    return False

# Validate that the flight specification has either one of the seating classes
def isTwelveDigitValid(flightSpec):
    twelveth = flightSpec[11]
    if twelveth == 'E' or twelveth == 'F':
        return True
    return False

# Function which validates the whole flight specification
def isValidSpec(flightSpec):
    return isValidSpecLength(flightSpec) and \
        isFourthDigitValid(flightSpec) and \
        isFifthDigitValid(flightSpec) and \
        isSixthDigitValid(flightSpec) and \
        isSeventhDigitValid(flightSpec) and \
        isNinthDigitValid(flightSpec) and \
        isTenthDigitValid(flightSpec) and \
        isEleventhDigitValid(flightSpec) and \
        isFirstThreeDigitsValid(flightSpec) and \
        isTwelveDigitValid(flightSpec)

# Function to check the flight destination
def getDestination(flightSpec):
    if flightSpec[0:3] == "GLA":
        return "Glasgow, Scotland"
    if flightSpec[0:3] == "AMS":
        return "Schiphol, Amsterdam"
    return 'Unknown destination'

global FlightCost

# Function to check flight cost for either locations
def getFlightCost(flightSpec):
    if flightSpec[0:3] == "GLA":
        FlightCost = 80.00
        return FlightCost
    if flightSpec[0:3] == "AMS":
        FlightCost = 150.00
        return FlightCost
    return -1

# Function to calculate the baggage costs for a passengers number of bags
def getBaggageCosts(flightSpec):
    if isFifthDigitValid(flightSpec) == True:
        totalBags = int(flightSpec[4])
    if totalBags > 0:
        BaggageCost = 20.00 * (totalBags - 1)
        return BaggageCost

    return 0.00

# Function to calculate the appropriate discounts for a passenger
def discounts(flightSpec):

    if int(flightSpec[6:8]) > 15:
        MealDiscount = 0.00
        flightDiscount = 0.00
        TotalDiscount = flightDiscount + MealDiscount
        return TotalDiscount

    elif int(flightSpec[6:8]) <= 15:
        flightDiscount = getFlightCost(flightSpec) / 2
        MealDiscount = 2.50
        TotalDiscount = flightDiscount + MealDiscount
        return TotalDiscount

# Function to calculate the meal costs
def MealCost(flightSpec):
    if flightSpec[9] == 'N':
        return 0
    if flightSpec[9] == 'S':
        return 10.00
    if flightSpec[9] == 'V':
        return 12.00

# Function which return the appropriate seating class
def getSeatingClass(flightSpec):
    if flightSpec[11] == 'E':
        return 'Economy'
    if flightSpec[11] == 'F':
        return 'First Class'

# Function which calculates the cost for a first class passenger or economy passenger
def totalCost(flightSpec):
    if flightSpec[11] == 'F':
        finalCost = (getFlightCost(flightSpec)*6) + getBaggageCosts(flightSpec) + MealCost(flightSpec) - discounts(flightSpec)
        return finalCost
    if flightSpec[11] == 'E':
        finalCost = getFlightCost(flightSpec) + getBaggageCosts(flightSpec) + MealCost(flightSpec) - discounts(flightSpec)
        return finalCost

# Function to print the flight specfication in a organised format
def getFlightDetails(flightSpec):
    if isValidSpec(flightSpec) == False:
        print('Invalid Flight Spec')
        return
    print('Destination: ' + str(getDestination(flightSpec)))
    print('Flight Cost: ' + str(getFlightCost(flightSpec)))
    print('Number of Bags: ' + str(flightSpec[4]))
    print('Baggage Cost: ' + str(getBaggageCosts(flightSpec)))
    print('Meal: ' + str(flightSpec[9]))
    print('Meal Cost: ' + str(MealCost(flightSpec)))
    print('Seating Class: ' + str(getSeatingClass(flightSpec)))
    print('Total Cost: ' + str(totalCost(flightSpec)))

flightSpec = str(input("Please enter a flight specfication? "))
getFlightDetails(flightSpec)