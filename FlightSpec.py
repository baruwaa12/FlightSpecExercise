def isValidSpecLength(flightSpec):
    if len(flightSpec) == 12:
        return True
    else:
        return False


def isFirstThreeDigitsValid(flightSpec):
    firstThree = flightSpec[0:3]
    if firstThree == "AMS" or firstThree == "GLA":
        return True
    return False


def isFourthDigitValid(flightSpec):
    fourth = flightSpec[3]
    if fourth == ' ':
        return True

    return False


def isFifthDigitValid(flightSpec):
    fifth = flightSpec[4]
    if fifth.isdigit() == False:
        return False
    else:
        if int(fifth) <= 3 and int(fifth) >= 0:
            return True


def isSixthDigitValid(flightSpec):
    sixth = flightSpec[5]
    if sixth == ' ':
        return True

    return False


def isSeventhDigitValid(flightSpec):
    seventh = flightSpec[6:7]
    if seventh.isdigit() == False:
        return False

    if int(seventh) <= 99 and int(seventh) >= 0:
        return True


def isNinthDigitValid(flightSpec):
    ninth = flightSpec[8]
    if ninth == ' ':
        return True

    return False


def isTenthDigitValid(flightSpec):
    tenth = flightSpec[9]
    if tenth == 'N' or tenth == 'S' or tenth == 'V':
        return True
    return False


def isEleventhDigitValid(flightSpec):
    eleventh = flightSpec[10]
    if eleventh == ' ':
        return True

    return False


def isTwelveDigitValid(flightSpec):
    twelveth = flightSpec[11]
    if twelveth == 'E' or twelveth == 'F':
        return True
    return False


def isValidSpec(flightSpec):
    if isValidSpecLength(flightSpec) and isFirstThreeDigitsValid(flightSpec) and isFourthDigitValid(flightSpec) and isFifthDigitValid(flightSpec) and isSixthDigitValid(flightSpec) and isSeventhDigitValid(flightSpec) and isNinthDigitValid(flightSpec) and isTenthDigitValid(flightSpec) and isEleventhDigitValid(flightSpec) and isTwelveDigitValid(flightSpec) == True:
        return True
    return False


def getDestination(flightSpec):
    if flightSpec[0:3] == "GLA":
        return "Glasgow, Scotland"
    if flightSpec[0:3] == "AMS":
        return "Schiphol, Amsterdam"
    return 'Unknown destination'


global FlightCost


def getFlightCost(flightSpec):
    if flightSpec[0:3] == "GLA":
        FlightCost = 80.00
        return FlightCost
    if flightSpec[0:3] == "AMS":
        FlightCost = 150.00
        return FlightCost
    return -1


def getBaggageCosts(flightSpec):
    if isFifthDigitValid(flightSpec) == True:
        totalBags = int(flightSpec[4])
    if totalBags > 0:
        BaggageCost = 20.00 * (totalBags - 1)
        return BaggageCost

    return 0.00


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


def MealCost(flightSpec):
    if flightSpec[9] == 'N':
        return 0
    if flightSpec[9] == 'S':
        return 10.00
    if flightSpec[9] == 'V':
        return 12.00


def getSeatingClass(flightSpec):
    if flightSpec[11] == 'E':
        return 'Economy'
    if flightSpec[11] == 'F':
        return 'First Class'

def totalCost(flightSpec):
    if flightSpec[11] == 'F':
        finalCost = (getFlightCost(flightSpec)*6) + getBaggageCosts(flightSpec) + MealCost(flightSpec) - discounts(flightSpec)
        return finalCost
    if flightSpec[11] == 'E':
        finalCost = getFlightCost(flightSpec) + getBaggageCosts(flightSpec) + MealCost(flightSpec) - discounts(flightSpec)
        return finalCost

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