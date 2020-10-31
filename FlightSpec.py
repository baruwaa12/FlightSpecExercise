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
    else:
        if int(seventh) <= 99 and int(seventh) >= 0:
            return True




def isValidSpec(flightSpec):
    return True