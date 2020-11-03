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
    FlightCost = 80.00
    destination = "Glasgow, Scotland"
else:
    FlightCost = 150.00 
    destination = "Schinphol, Amsterdam"
    print(destination)


## Part B - Baggage Costs

if isFifthDigitValid(flightSpec) == True:
    totalBags = int(flightSpec[4])
    if totalBags > 0:
        BaggageCost = 20.00 * (totalBags - 1)
        print(BaggageCost)
    else:
        BaggageCost = 0
        print(BaggageCost)


## Part C - Child Discounts

Child = bool
if isSeventhDigitValid(flightSpec) == True:
    if int(flightSpec[6:7]) <= 15:
        Discounts = (2.5 + FlightCost/2)
        Child(True)
    else:
        Discounts = 0 
        Child(False)

## Part D - Meals
if isTenthDigitValid(flightSpec) == True:
    MealType = flightSpec[9]
    if MealType == 'S':
        Meal = 'Standard'
        MealCost = 10.00
    elif MealType == 'V':
        MealCost = 12.00
        Meal = 'Vegetarian'
    else:
        MealCost = 0

## Part E - Seating Class

if isEleventhDigitValid(flightSpec) == True:
    if flightSpec[11] == 'E':
        SeatingClass = 'Economy'
        SeatingCost = 0
        Final_Cost = (FlightCost + BaggageCost + MealCost + SeatingCost) - Discounts
    else:
        SeatingClass = 'First Class'
        MealCost = 0
        Final_Cost = ((FlightCost * 6) + BaggageCost + MealCost + SeatingCost) - Discounts




print("Destination: " + str(destination))
print("Flight Cost: " + str(FlightCost))
print("Number of Bags: " + str(totalBags))
print("Baggage Cost: " + str(BaggageCost))
print("Child: " + str(Child))
print("Meal: " + str(MealType))
print("Meal Cost: " + str(MealCost))
print("Seating Class: " + str(SeatingClass))
print("Total Cost: " + str(Final_Cost))