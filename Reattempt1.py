## User enters Flight Specification
## Check if the entry fits the required length of for the program - GLA 0 25 S E

flightSpec = str(input("Enter a flight specification? "))

if len(flightSpec) < 12:
  return ("Incorrect specification length, restart program and enter again.")

## Find the number of bags and calculate the bag cost

numOfBags = int(flightSpec[4])
bagCost = 0

if numOfBags <= 1:
    bagCost = bagCost
    print(bagCost)
else:
    bagCost = (numOfBags - 1) * 20
    print(bagCost)


## Check for the destination
## Find out the current flight cost and see if the child discount can be applied
## Check an appropriate age has been given.
  
BasicFlightCostAMS = 150
BasicFlightCostGLA = 80
CurrentFlightCost = 0

passAge = int(flightSpec[6:8])
destination = str(flightSpec[0:3])

if passAge <= 0 or passAge > 99:
  return "Unrealistic age given, restart program and try again. "

if destination == "GLA":
  if passAge <= 15:
    CurrentFlightCost = BasicFlightCostGLA / 2
  else:
    CurrentFlightCost = BasicFlightCostGLA

if destination == "AMS":
  if passAge <= 15:
    CurrentFlightCost = BasicFlightCostAMS / 2
  else:
    CurrentFlightCost = BasicFlightCostAMS


## Find out what meal was chosen.
## Determine if a child discount can be applied to meal cost 
MealCostS = 10
MealCostV = 12
FinalMealCost = 0

MealChosen = str(flightSpec[9])

if MealChosen == "S":
  if passAge <= 15:
    FinalMealCost = MealCostS - 2.50
    print(FinalMealCost)
  else:
    FinalMealCost = MealCostS

if MealChosen == "V":
  if passAge <= 15:
    FinalMealCost = MealCostV - 2.50
  else:
    FinalMealCost = MealCostV


## Determine the Seating Class and the final basic flight cost
SeatType = flightSpec[11]
FinalFlightCost = 0

if SeatType == "F":
  FinalBasicFlightCost = CurrentFlightCost * 6
  print(FinalBasicFlightCost)
else:
  FinalBasicFlightCost = CurrentFlightCost
  print(FinalBasicFlightCost)

## Continue testing.
## Think of ways that program can break.
  
