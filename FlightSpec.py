def isValidSpecLength(flightSpec):
    if len(flightSpec) == 12:
        return True
    else:
        return False

def isFirstThreeDigitsValid(flightSpec):
    firstThree = flightSpec[0:3]
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
    return True