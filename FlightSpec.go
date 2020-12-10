package flightSpecExercise

import (
	"fmt"
	"strconv"
)

// SpecLength to find the length of the Spec string
func SpecLength(input string) bool {
	if len(input) < 12 {
		return false 
		}
	return true
	}

// LocationFinder determines the location from the Spec string 
func LocationFinder(input string) string {
	location := input[0:3]
	if location == "GLA" {
		location = "Glasgow"
		fmt.Println(location)
	} else {
		location = "Amsterdam"
		fmt.Println(location)
	}
	return location
}

// PassengerAge function makes sure the age is between 0 and 99
func PassengerAge(input string) int {
	age := input[6:8]
	fmt.Println(age)
	Age, _ := strconv.Atoi(age)
	if Age < 0 {
		fmt.Println("Not possible")
	}
	if Age > 99 {
		fmt.Println("Not possible")
	}
	return Age
}

// PassengerMeal function determines whether the spec has one of these symbols.
func PassengerMeal(input string) string {
	Meal := input[9]
	if Meal == 'S' {
		Meal := "Standard"
		return Meal
	}
	if Meal == 'N'{
		Meal := "None"
		return Meal
	}
	if Meal == 'V' {
		Meal := "Vegetarian"
		return Meal
	}else{
		return "This symbol does not represent any meal"
	}
}

// PassengerSeatClass determines if seat in the spec is either economy or first class
func PassengerSeatClass(input string) string {
	SeatClass := input[11]
	if SeatClass == 'E' {
		SeatClass := "Economy"
		return SeatClass
	}
	if SeatClass  == 'F' {
		SeatClass := "First Class"
		return SeatClass
	}
	return "This is not a valid class"
}

// PassengerBaggage determines how much luggage a passenger has.
func PassengerBaggage(input string) string {
	NumBaggage := byte(input[4])
	numofbaggage := int(NumBaggage)

	if numofbaggage >= 0 && numofbaggage <= 9 {
		return "This number of baggage is valid"
	}

	return "This number of baggage is invalid"
}
