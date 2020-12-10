package flightSpecExercise

import (
	"testing"
)

func TestFlightSpec(t * testing.T) {
	for _, test := range testCases {
		if actual := SpecLength(test.input); actual != test.expected {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)

	}
}

func TestLocationFinder(t * testing.T) {
	for _, test := range testCases {
		if actual := LocationFinder(test.input); actual != test.location {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)
	}
}

func TestPassengerAge(t * testing.T) {
	for _, test := range testCases {
		if actual := PassengerAge(test.input); actual != test.age {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)
	}
}

func TestPassengerMeal(t * testing.T) {
	for _, test := range testCases {
		if actual := PassengerMeal(test.input); actual != test.meal {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)
	}
}

func TestPassengerSeatClass(t * testing.T) {
	for _, test := range testCases {
		if actual := PassengerSeatClass(test.input); actual != test.seating {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)
	}
}

func TestPassengerBaggage(t * testing.T) {
	for _, test := range testCases {
		if actual := PassengerBaggage(test.input); actual != test.baggage {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)
	}
}

