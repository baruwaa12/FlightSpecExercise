def isValidSpecLength(flightSpec):
    if len(flightSpec) == 12:
        return True
    else:
        return False

def isFirstThreeDigitsValid(flightSpec):
    firstThree = flightSpec[0:3]
    if firstThree == "AMS" or firstThree == "GLA":
        return firstThree.isalpha()

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
    if isValidSpecLength("AMS 0 25 S E") + isFirstThreeDigitsValid("AMS 0 25 S E") + isFourthDigitValid("AMS 0 25 S E") + isFifthDigitValid("AMS 0 25 S E") + isSixthDigitValid("AMS 0 25 S E") + isSeventhDigitValid("AMS 0 25 S E") + isNinthDigitValid("AMS 0 25 S E") + isTenthDigitValid("AMS 0 25 S E") + isEleventhDigitValid("AMS 0 25 S E") + isTwelveDigitValid("AMS 0 25 S E") == True:
        return True
    return False


## Part A - User Input and Flight Destination


flightSpec = str(input("Please enter a flight specfication?"))
if isFirstThreeDigitsValid(flightSpec) == "GLA":
    FlightCost = 80
    destination = "Glasgow, Scotland"
else:
    FlightCost = 150
    destination = "Schinphol, Amsterdam"
    print(destination)


## Part B - Baggage Costs

if isFifthDigitValid(flightSpec) == True:
    totalBags = int(flightSpec[4])
    if totalBags > 0:
        BaggageCost = 20 * (totalBags - 1)
    else:
        BaggageCost = 0
        print(BaggageCost)





    





