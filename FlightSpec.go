package flightSpecExercise

import (
	"fmt"
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